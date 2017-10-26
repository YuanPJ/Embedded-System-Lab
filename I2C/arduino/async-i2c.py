#!/usr/bin/python
import smbus
import time
import RPi.GPIO as GPIO

bus = smbus.SMBus(1)
address = 0x04
TRIGGER_PIN = 17

def writeNumber(value):
    bus.write_byte(address, value)
    print "RPI: Hi Arduino, I sent you ", var
    return -1

def readNumber(channel):
    number = bus.read_byte(address)
    print  "Arduino: Hey RPI, I received a digit ", number
    return -1

if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(TRIGGER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    
    GPIO.add_event_detect(TRIGGER_PIN, GPIO.BOTH, callback=readNumber, bouncetime=200)

    while True:
        var = input("Enter 1 - 255:")
        if not var:
            continue
        writeNumber(var)
        time.sleep(1)
