# Reading the 3D acceleator value

Before using any of the code below, please ensure that the ADXL345 module is correctly connected to the Raspberry Pi and not malfunctioning.

The Python code is named `adxl345.py` here, requiring `smbus` and Python 2.7.

Usage:
	
	$ python adxl345.py

The C code is named `ADXL345.c` here, requiring `wiringPi`.

Usage:
	
	$ make
	$ ./ADXL345
