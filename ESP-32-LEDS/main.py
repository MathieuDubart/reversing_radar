# from bluetooth_manager import *

# # remplacer central par inbstance BTManager
# bleManager = BluetoothManager(lowParam = 0, highParam = 40)

# try:
#   bleManager.connect()
#   while True:
#     if bleManager.central.is_connected():
#       bleManager.receive()

# except KeyboardInterrupt:
#     pass

# import machine, neopixel

# nbLeds = 4
# pin1 = 27
# pin2 = 19
# pin3 = 32
# pin4 = 23
# pin5 = 0

# np1 = neopixel.NeoPixel(machine.Pin(pin1), nbLeds)
# np2 = neopixel.NeoPixel(machine.Pin(pin2), nbLeds)
# np3 = neopixel.NeoPixel(machine.Pin(pin3), nbLeds)
# np4 = neopixel.NeoPixel(machine.Pin(pin4), nbLeds)
# np5 = neopixel.NeoPixel(machine.Pin(pin5), nbLeds)


# np1[0] = (255, 0, 0)
# np1[1] = (255, 0, 0)
# np1[2] = (255, 0, 0)
# np1[3] = (255, 0, 0)

# np2[0] = (0, 255, 0)
# np2[1] = (0, 255, 0)
# np2[2] = (0, 255, 0)
# np2[3] = (0, 255, 0)

# np3[0] = (0, 0, 255)
# np3[1] = (0, 0, 255)
# np3[2] = (0, 0, 255)
# np3[3] = (0, 0, 255)

# np4[0] = (137, 201, 48)
# np4[1] = (137, 201, 48)
# np4[2] = (137, 201, 48)
# np4[3] = (137, 201, 48)

# np5[0] = (0, 255, 17)
# np5[1] = (255, 234, 0)
# np5[2] = (255, 115, 0)
# np5[3] = (255, 0, 0)


# while True:
#     np1.write()
#     np2.write()
#     np3.write()
#     np4.write()
#     np5.write()
