i = 0
while i < len(valuesArray):
  if int(valuesArray[i]) >= self.highParam:
    print(int(valuesArray[i]))
    self.sensorsLeds[i][0] = (0, 255, 0)
    self.vibrationMotor.value(0)
    self.sensorsLeds[i].write()

  elif self.lowParam < int(valuesArray[i]) < self.highParam:
    print(int(valuesArray[i]))
    currentLed = 0
    while currentLed < self.nofLeds:
      self.sensorsLeds[i][currentLed] = (255, 0, 0)
      self.vibrationMotor.value(1)
      self.sensorsLeds[i].write()
      currentLed += 1

  else:
    print(int(valuesArray[i]))
    currentLed = 0
    while currentLed < self.nofLeds:
      self.sensorsLeds[i][currentLed] = (0,0,0)
      self.vibrationMotor.value(0)
      currentLed += 1

  print('#####', i, '#####')
  i+=1




[NeoPixel(Pin(27), self.nofLeds),
NeoPixel(Pin(19), self.nofLeds),
NeoPixel(Pin(32), self.nofLeds),
NeoPixel(Pin(23), self.nofLeds),
NeoPixel(Pin(0), self.nofLeds)]



















from ble_simple_central import *
from padManager import *
import bluetooth
from time import sleep
from ble_simple_peripheral import *

class BluetoothManager():
  def __init__(self, lowParam = 40, highParam = 80, nofLeds = 4):
    self.ble = bluetooth.BLE()
    self.blePeripheral = BLESimplePeripheral(self.ble, name="pad")
    self.central = BLESimpleCentral(self.ble)
    self.not_found = False
    self.padManager = PadManager(lowParam = lowParam, highParam = highParam, nofLeds = nofLeds)


  def _on_scan(self, addr_type, addr, name):
    if addr_type is not None:
      print("Found peripheral:", addr_type, addr, name)
      self.central.connect()
    else:
      self.not_found = True
      print("No peripheral found.")
          
  def _scan(self):
    self.central.scan(callback=self._on_scan)

  def connect(self):
    self._scan()
    # Wait for connection...
    while not self.central.is_connected():
      sleep(1)
      if self.not_found:
        break
    
  def _isAck(self,v):
    v = v.decode('UTF-8')
    if v == "ack-radar":
      return True
    else:
      return False
    
  def send(self,data):
    self.blePeripheral.send(data)
    print("Message send:", data)
    
  def _decrypt(self, v):
    string = v.decode('UTF-8')
    array = string.split('#')
    return array
  
  def _delegateToPad(self, valuesArray):
    self.padManager.delegate(valuesArray = valuesArray)

  def _on_rx(self,v):
    if self._isAck(bytes(v)):
      print("Ack received")
    else:
      self._delegateToPad(self._decrypt(bytes(v)))

  def receive(self):
    self.central.on_notify(self._on_rx) 