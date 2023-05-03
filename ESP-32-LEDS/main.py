from sensorManager import *
from time import sleep
from ble_simple_central import *
import bluetooth


ble = bluetooth.BLE()
central = BLESimpleCentral(ble)

not_found = False

def on_scan(addr_type, addr, name):
    if addr_type is not None:
        print("Found peripheral:", addr_type, addr, name)
        central.connect()
    else:
        not_found = True
        print("No peripheral found.")
        
central.scan(callback=on_scan)

# Wait for connection...
while not central.is_connected():
    time.sleep(1)
    if not_found:
        break

print("Connected")

def on_rx(v):
    print("RX", bytes(v))

central.on_notify(on_rx)

with_response = False

i = 0
while central.is_connected():
    try:
        v = str(i) + "_"
        print("TX", v)
        central.write(v, with_response)
    except:
        print("TX failed")
    i += 1
    time.sleep_ms(5000 if with_response else 5000)

print("Disconnected")

