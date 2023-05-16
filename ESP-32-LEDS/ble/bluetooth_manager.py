from sensorManager import *
from time import sleep
from ble_simple_central import *
import bluetooth
from machine import Pin

class BluetoothManager():
  def __init__(self):
    self.ble = bluetooth.BLE()
    self.central = BLESimpleCentral(self.ble)
    self.not_found = False

    self.sensorsLeds= [[Pin(22, Pin.OUT), Pin(15, Pin.OUT)],
                      [Pin(19, Pin.OUT), Pin(18, Pin.OUT)],
                      [Pin(17, Pin.OUT), Pin(4, Pin.OUT)],
                      [Pin(26, Pin.OUT), Pin(14, Pin.OUT)]]

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

    print("Connected")
    
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
      if int(array[i]) >= 20:
        print(int(array[i]))
        self.sensorsLeds[i][0].value(0)
        self.sensorsLeds[i][1].value(1)
      elif 0 < int(array[i]) < 20:
        print(int(array[i]))
        self.sensorsLeds[i][0].value(1)
        self.sensorsLeds[i][1].value(0)
      else:
        print(int(array[i]))
        self.sensorsLeds[i][0].value(0)
        self.sensorsLeds[i][1].value(1)

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
