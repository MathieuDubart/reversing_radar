from sensorManager import *
from time import sleep
from ble_simple_central import *
import bluetooth
import machine

class BluetoothManager():
  def __init__(self):
    self.ble = bluetooth.BLE()
    self.central = BLESimpleCentral(self.ble)
    self.not_found = False
    # self.sensorsLeds= [[Pin(22, Pin.OUT), Pin(15, Pin.OUT)],
                      #  [Pin(19, Pin.OUT), Pin(18, Pin.OUT)],
                      #  [Pin(17, Pin.OUT), Pin(4, Pin.OUT)],
                      #  [Pin(26, Pin.OUT), Pin(14, Pin.OUT)]]

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
  
  def _decrypt(self, v):
    string = v.decode('UTF-8')
    array = string.split('#')
    return array
  
  def _tunrOnLeds(self, array):
    i = 0
    while i < len(array):
      if int(array[i]) >= 40:
        print('Far')
        # self.sensorsLeds[i][0].value(1)
        # self.sensorsLeds[i][1].value(0)
      elif 0 < int(array[i]) < 40:
        print('Near')
        # self.sensorsLeds[i][0].value(0)
        # self.sensorsLeds[i][1].value(1)
      else:
        print('Out of range')
        # self.sensorsLeds[i][0].value(0)
        # self.sensorsLeds[i][1].value(0)
        
      i+=1
        
  def _on_rx(self,v):
    self._tunrOnLeds(self._decrypt(bytes(v)))


  def receive(self):
    self.central.on_notify(self._on_rx)
  
  
  print("Disconnected")