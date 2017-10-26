import smbus
from time import sleep

# select the correct i2c bus for this revision of Raspberry Pi
bus = smbus.SMBus(1)

# ADXL345 constants
EARTH_GRAVITY_MS2   = 9.80665
SCALE_MULTIPLIER    = 0.004

DATA_FORMAT         = 0x31
BW_RATE             = 0x2C
POWER_CTL           = 0x2D 

# Bandwidth rates
BW_RATE_1600HZ      = 0x0F
BW_RATE_800HZ       = 0x0E
BW_RATE_400HZ       = 0x0D
BW_RATE_200HZ       = 0x0C
BW_RATE_100HZ       = 0x0B
BW_RATE_50HZ        = 0x0A
BW_RATE_25HZ        = 0x09

RANGE_2G            = 0x00
RANGE_4G            = 0x01
RANGE_8G            = 0x02
RANGE_16G           = 0x03

MEASURE             = 0x08
AXES_DATA           = 0x32

def init(address = 0x53):
    
    # Set Bandwidth RATE
    bus.write_byte_data(address, BW_RATE, BW_RATE_200HZ)

    # Set measurement range for 10-bit reading
    value = bus.read_byte_data(address, DATA_FORMAT)
    value &= ~0x0F
    value |= RANGE_2G
    value |= 0x08
    bus.write_byte_data(address, DATA_FORMAT, value)

    # Set power control to measure mode
    bus.write_byte_data(address, POWER_CTL, MEASURE)

def getAxes(gforce = False):
    bytes = bus.read_i2c_block_data(address, AXES_DATA, 6)
    
    x = bytes[0] | (bytes[1] << 8)
    if(x & (1 << 16 - 1)):
        x = x - (1<<16)

    y = bytes[2] | (bytes[3] << 8)
    if(y & (1 << 16 - 1)):
        y = y - (1<<16)

    z = bytes[4] | (bytes[5] << 8)
    if(z & (1 << 16 - 1)):
        z = z - (1<<16)

    x = x * SCALE_MULTIPLIER 
    y = y * SCALE_MULTIPLIER
    z = z * SCALE_MULTIPLIER

    if gforce == False:
        x = x * EARTH_GRAVITY_MS2
        y = y * EARTH_GRAVITY_MS2
        z = z * EARTH_GRAVITY_MS2

    x = round(x, 4)
    y = round(y, 4)
    z = round(z, 4)

    return {"x": x, "y": y, "z": z}

if __name__ == "__main__":
    address = 0x53
    init(address)
    while True:
        axes = getAxes(True)
        print "ADXL345 on address 0x%x:" % address
        print "   x = %.3fG" % ( axes['x'] )
        print "   y = %.3fG" % ( axes['y'] )
        print "   z = %.3fG" % ( axes['z'] )
        sleep(0.5)
