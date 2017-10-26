# Reading the 3D acceleator value

Before using any of the code below, please ensure that the Arduino is correctly connected to the Raspberry Pi and the corresponding arudino code is uploaded.

| RPi 3                | Arduino UNO     |
|----------------------|-----------------|	
| GPIO 2 (pin 3) (SDA) |  Analog 4 (SDA) |
| GPIO 3 (pin 5) (SCL) |  Analog 5 (SCL) |
| GPIO 17              |  Digital 8      |
| GND	               |  GND            |

## Raspberry Pi side
The Python code is named `async-i2c.py` here, requiring [`RPi.GPIO`](https://pypi.python.org/pypi/RPi.GPIO) and Python 2.7.

Usage:

    $ python async-i2c.py

The C code is named `async-i2c.c` here, requiring `wiringPi`.

Usage:

    $ make
    $ ./ADXL345

## Arduino side
The arduino side code is named `arduino.ino` here.
