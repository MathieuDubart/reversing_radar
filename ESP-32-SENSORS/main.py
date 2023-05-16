from time import sleep_ms
import bluetooth
import random
import struct
import time
from hcsr04 import *
from wireless_manager import *
from connectionCheckersSensors import *
from connectionStates import *

class BLECallback(CommunicationCallback):

    def __init__(self,bleName="sensors"):
        self.bleName = bleName
        self.wirelessManager = None
    
    def connectionCallback(self):
        print("Connected")
    
    def disconnectionCallback(self):
        print("Disconected")
    
    def didReceiveCallback(self,value):
        if value == "ack":
            self.wirelessManager.send("ack")
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

wirelessManager = WirelessManager(BLECallback("sensors"))
bleStateManager = BleStateManager(BleConnectionChecker, wirelessManager, 3)

bleStateManager.process()
try:
    while True:
        sleep_ms(100)
        #wirelessManager.send("{}#{}#{}#{}".format(sensor1.getDistance(), sensor2.getDistance(), sensor3.getDistance(), sensor4.getDistance()))
            
except KeyboardInterrupt:
    pass