# BLE Programming

Use 2 Raspberry Pi devices to simulate the scene of BLE central and BLE sensor device. The central is able to fetch data from the peripheral device (sensor) via bluetootch communication.

Using DHT11 sensor for the sensor device to query the air temperature and relative humidity.

## Dependencies
- Central: Python2.7, [pygattlib](https://bitbucket.org/OscarAcena/pygattlib)
- Peripheral: Node.js, [bleno](https://github.com/sandeepmistry/bleno), [node-dht-sensor](https://github.com/momenso/node-dht-sensor)

## Peripheral side
Before set up the bluetootch service, please ensure that DHT11 is properly connected to the RPi.

The source code is `main.js` and `characteristic.js`.

### Usage
Make the BLE peripheral scannable

    $ sudo hciconfig hci0 up
    $ sudo hciconfig hci0 leadv 0

Check the device bluetootch address by

    $ hciconfig

and modify the address variable in `central.py` to ensure that the central can correctly connect to the sensor.

After the setup use the following command to build up the service, `sudo` is required as permission to access the bluetootch chip directly is needed.

    $ sudo node main.js

## Central side

The source code is `central.py`.

### Usage
Use the command

    $ sudo python central.py

and the data should be shown.

Notice: First time of fetch may collect incorrect data, repeat fetching to solve the problem.
