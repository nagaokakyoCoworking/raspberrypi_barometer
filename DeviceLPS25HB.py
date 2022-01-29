#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# DeviceLPS25HB
#
#   LPS25HB (STMicroelectronics)
#   MEMS pressure sensor: 260-1260 hPa absolute digital output barometer
#
#
#


class DeviceLPS25HB:
    device = None
    WHO_AM_I = 0x0f
    PRESS_OUT_XL = 0x28
    PRESS_OUT_L = 0x29
    PRESS_OUT_H = 0x2a
    TEMP_OUT_L = 0x2b
    TEMP_OUT_H = 0x2c

    CTRL_REG1 = 0x20
    CTRL_REG2 = 0x21
    CTRL_REG3 = 0x22
    CTRL_REG4 = 0x23

    I2C_ADDRESS_1 = 0x5d
    I2C_ADDRESS_2 = 0x5c

    def __init__(self, device):
        self.device = device

    def init(self, address):
        """
        デバイスを初期化する
        :param address: I2C の時は、アドレス、SPI の場合はダミー値で 0x00
        :return:
        """
        pass

    def write_data(self, address, data) -> bytes:
        """
        指定したアドレスに 送出する値 を送出し、受信データを受け取る
        :param address: I2C の時は、アドレス、SPI の場合はダミー値で 0x00
        :param data: 送出するデータ
        :return:
        """
        pass

    def get_pressure_value(self, address) -> float:
        """
        気圧の値を取得する
        :param address: I2C の時は、アドレス、SPI の場合はダミー値で 0x00
        :return: 気圧 [hPa]
        """
        pressure_h = self.write_data(address, self.PRESS_OUT_H)
        pressure_l = self.write_data(address, self.PRESS_OUT_L)
        pressure_xl = self.write_data(address, self.PRESS_OUT_XL)
        ret = (pressure_h << 16) + (pressure_l << 8) + pressure_xl
        ret = ret / 4096
        return ret

    def get_temperature_value(self, address) -> float:
        """
        気温の値を取得する
        :param address: I2C の時は、アドレス、SPI の場合はダミー値で 0x00
        :return: 気温 [℃]
        """
        temperature_h = self.write_data(address, self.TEMP_OUT_H)
        temperature_l = self.write_data(address, self.TEMP_OUT_L)
        ret = (temperature_h << 8) + temperature_l
        # 2の補数 から変換
        if ret > 0x7fff:
            ret = ret - 0x10000
        ret = 42.5 + (ret / 480)
        return ret
