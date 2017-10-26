var util = require('util');

var bleno = require('bleno');

var sensor = require('node-dht-sensor');

var BlenoCharacteristic = bleno.Characteristic;

const SENSOR_PIN = 4;

var EchoCharacteristic = function() {
  EchoCharacteristic.super_.call(this, {
    uuid: '1902',
    properties: ['read'],
    value: null
  });

  this._data = new Buffer(0);
  this._updateValueCallback = null;
};




util.inherits(EchoCharacteristic, BlenoCharacteristic);

var temp = 0, hum = 0;

EchoCharacteristic.prototype.onReadRequest = function(offset, callback) {
    sensor.read(11, SENSOR_PIN, (err, temperature, humidity) => {
	    console.log(temp.toFixed(1))
	    temp = temperature;
	    hum = humidity;
    })
	this._data = new Buffer(2);
	this._data.fill(0);
	this._data.writeInt8(temp, 0);
	this._data.writeInt8(hum, 1);
    
 console.log('EchoCharacteristic - onReadRequest: value = ' + temp.toString() + hum.toString());

  callback(this.RESULT_SUCCESS, this._data);
};

module.exports = EchoCharacteristic;
