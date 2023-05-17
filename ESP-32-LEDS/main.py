from bluetooth_manager import *

# remplacer central par inbstance BTManager
bleManager = BluetoothManager(lowParam = 40)

try:
  bleManager.connect()
  while True:
    if bleManager.central.is_connected():
      bleManager.receive()

except KeyboardInterrupt:
    pass

# import machine, neopixel

# nbLeds = 4
# pin = 27

# np = neopixel.NeoPixel(machine.Pin(p), n)

# np[0] = (255, 0, 0)
# np[1] = (125, 204, 223)
# np[2] = (120, 153, 23)
# np[3] = (255, 0, 153)

# while True:
#     np.write()