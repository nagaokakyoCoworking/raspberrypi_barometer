#!/usr/bin/python
#
# LPS25HB (I2C 通信)
#
import DeviceLPS25HB


class I2cDeviceLPS25HB(DeviceLPS25HB.DeviceLPS25HB):

    def write_data(self, address, data) -> bytes:
        return self.device.read_byte_data(address, data)

    def init(self, address):
        received_value = self.write_data(address, self.WHO_AM_I)
        if received_value == 0xbd:
            # PDi  (b7)    = 1
            # ODR  (b6-b4) = 010
            # DIFF_EN (b3) = 0
            # BDU      (b2)= 0
            # RESET_AZ (b1)= 0
            # SIM      (b0)= 0
            self.device.write_byte_data(address, self.CTRL_REG1, 0xc0 )
            ret = True
        else:
            ret = False
        return ret
