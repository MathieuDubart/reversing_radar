from sensorManager import *
from time import sleep
from ble_simple_central import *
import bluetooth
from machine import Pin
import neopixel

class BluetoothManager():
  def __init__(self):
    self.ble = bluetooth.BLE()
    self.central = BLESimpleCentral(self.ble)
    self.not_found = False
    self.nofLeds = 4
    self.sensorsLeds = [neopixel.NeoPixel(Pin(24), self.nofLeds),
                      neopixel.NeoPixel(Pin(25), self.nofLeds),
                      neopixel.NeoPixel(Pin(26), self.nofLeds),
                      neopixel.NeoPixel(Pin(27), self.nofLeds)]
    self.vibrationMotor = Pin(28, Pin.OUT)

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
    if v == "ack":
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
  

  def _turnOnLeds(self, array):
    i = 0
    while i < len(array):
      if int(array[i]) >= 40:
        print(int(array[i]))
        self.sensorsLeds[i][0] = (0, 255, 0)
        self.vibrationMotor.value(0)
        self.sensorsLeds[i].write()
      elif 0 < int(array[i]) < 40:
        print(int(array[i]))
        currentLed = 0
        while currentLed < len(self.nofLeds):
          self.sensorsLeds[i][currentLed] = (255, 0, 0)
          self.vibrationMotor.value(1)
          self.sensorsLeds[i].write()
          currentLed += 1
      else:
        print(int(array[i]))
        currentLed = 0
        while currentLed < len(self.nofLeds):
          self.sensorsLeds[i][currentLed] = ''
          self.vibrationMotor.value(0)
          currentLed += 1

      print('#####', i, '#####')
      i+=1
        
  def _on_rx(self,v):
    if self._isAck(bytes(v)):
      print("Ack received")
    else:
      self._turnOnLeds(self._decrypt(bytes(v)))

  def receive(self):
    self.central.on_notify(self._on_rx) 
  
  
  print("Disconnected")
