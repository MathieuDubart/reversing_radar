from time import sleep_ms
import bluetooth
import random
import struct
import time
from hcsr04 import *
from sensorManager import *
from wireless_manager import *

class BLECallback(CommunicationCallback):

    def __init__(self,bleName="default"):
        self.bleName = bleName
    
    def connectionCallback(self):
        print("Connected")
    
    def disconnectionCallback(self):
        print("Disconected")
    
    def didReceiveCallback(self,value):
        print(f"Received {value}")
    

sensor1 = HCSR04(trigger_pin=33, echo_pin=25, echo_timeout_us=10000)
# redLed1 = Pin(22, Pin.OUT)
# greenLed1 = Pin(15, Pin.OUT)

sensor2 = HCSR04(trigger_pin=32, echo_pin=35, echo_timeout_us=10000)
# redLed2 = Pin(19, Pin.OUT)
# greenLed2 = Pin(18, Pin.OUT)

sensor3 = HCSR04(trigger_pin=16, echo_pin=4, echo_timeout_us=10000)
# redLed3 = Pin(17, Pin.OUT)
# greenLed3 = Pin(4, Pin.OUT)

sensor4 = HCSR04(trigger_pin=21, echo_pin=19, echo_timeout_us=10000)
# redLed4 = Pin(26, Pin.OUT)
# greenLed4 = Pin(14, Pin.OUT)

# sensorManager1 = SensorManager(sensor1, redLed1, greenLed1)
# sensorManage2 = SensorManager(sensor2, redLed1, greenLed1)
# sensorManager3 = SensorManager(sensor3, redLed1, greenLed1)
# sensorManager4 = SensorManager(sensor4, redLed1, greenLed1)

    
wirelessManager = WirelessManager(BLECallback())

try:
    while True:
        #distance = sensor.distance_cm()
        #sensorManager.estimateDistance()
        #print("A:",sensor1.getDistance())
        #print("B:",sensor2.getDistance())
        # print("C:",sensor3.getDistance())
        # print("D:",sensor4.getDistance())

        sleep_ms(100)
        
        wirelessManager.sendDataToBLE("Hoho BLE")
            
except KeyboardInterrupt:
    pass