#!/usr/bin/python

from I2cDeviceLPS25HB import I2cDeviceLPS25HB,DeviceLPS25HB
import smbus
import time
import requests

i2c = smbus.SMBus(1)
device = I2cDeviceLPS25HB(i2c)
address = I2cDeviceLPS25HB.I2C_ADDRESS_2


if device.init(address) == True:
    time.sleep(1)
    pressure = device.get_pressure_value(address)
    temperature =device.get_temperature_value(address)
    # save to database
