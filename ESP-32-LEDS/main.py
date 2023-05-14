from bluetooth_manager import *

# remplacer central par inbstance BTManager
ble = BluetoothManager()
ble.connect()
while True:
  if ble.central.is_connected():
    ble.receive()