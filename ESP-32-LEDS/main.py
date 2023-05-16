from bluetooth_manager import *

# remplacer central par inbstance BTManager
bleManager = BluetoothManager()

try:
  bleManager.connect()
  while True:
    if bleManager.central.is_connected():
      bleManager.receive()

except KeyboardInterrupt:
    pass