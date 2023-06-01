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
        print("message received:", value)
        return value
    

sensor1 = HCSR04(trigger_pin=32, echo_pin=34, echo_timeout_us=10000)
sensor2 = HCSR04(trigger_pin=25, echo_pin=33, echo_timeout_us=10000)
sensor3 = HCSR04(trigger_pin=14, echo_pin=12, echo_timeout_us=10000)
sensor4 = HCSR04(trigger_pin=19, echo_pin=18, echo_timeout_us=10000)
sensor5 = HCSR04(trigger_pin=16, echo_pin=4, echo_timeout_us=10000)
sensor6 = HCSR04(trigger_pin=15, echo_pin=2, echo_timeout_us=10000)

wirelessManager = WirelessManager(BLECallback("sensors"))
bleStateManager = BleStateManager(BleConnectionChecker, AckChecker, wirelessManager, 3)

bleStateManager.process()
try:
    bleStateManager.process()
    if type(bleStateManager.currentState) == BleIsReady:
        while True:
            sleep_ms(1000)
            wirelessManager.send("{}#{}#{}#{}#{}#{}".format(sensor1.getDistance(), sensor2.getDistance(), sensor3.getDistance(), sensor4.getDistance(), sensor5.getDistance(), sensor6.getDistance()))
            
except KeyboardInterrupt:
    pass