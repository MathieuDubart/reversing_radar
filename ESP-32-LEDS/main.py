from bluetooth_manager import *

# remplacer central par inbstance BTManager
bleManager = BluetoothManager(lowParam = 40, highParam = 80, nofLeds = 4)

try:
  bleManager.connect()
  while True:
    if bleManager.central.is_connected():
      bleManager.receive()

except KeyboardInterrupt:
    pass
