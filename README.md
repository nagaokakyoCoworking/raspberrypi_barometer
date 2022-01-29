# Raspberry Pi と 超小型気圧センサー LPS25HB (STMicroelectronics) を使った気圧ロガー

https://coworking-nagaokakyo.jp/note/post-2866/

## 回路図

Raspberry Pi とセンサーモジュールとは、I2C インターフェースを使って通信を行います。SA0 ピンをGNDに接続しているので、スレーブアドレスは、 1011100x になります。

![回路図](https://coworking-nagaokakyo.jp/wp-content/uploads/2022/01/raspberrypi_barometer.png)

### 実体配線

![実体配線](https://coworking-nagaokakyo.jp/wp-content/uploads/2022/01/DSC_0096-scaled.jpg)

## 使い方

以下のファイルを Raspberry Pi にアップロードをする。

* DeviceLPS25HB.py
* I2cDeviceLPS25HB.py
* barometer.py

barometer.py のプログラムを任意のデータ保存場所に保存する処理に変更して、cron で barometer.py を実行するとロガーの完成です。

### 測定結果例

![測定結果例](https://coworking-nagaokakyo.jp/wp-content/uploads/2022/01/raspberrypi_barometer_results.png)


## 免責事項

回路図やプログラムは、電子工作のために作成したもので、それを用いたことによって生じた損害については、一切責任は負うことはできません。
あらかじめご了承をお願いいたします。
