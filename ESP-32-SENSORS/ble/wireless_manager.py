from time import sleep

class CommunicationCallback:
    
    def __init__(self):
        pass
    
    def connectionCallback(self):
        print("Connected")
    
    def disconnectionCallback(self):
        print("Disconected")
    
    def didReceiveCallback(self,value):
        print(f"Received {value}")
    
    
class WirelessManager:
    
    def __init__(self,bleCallback = None):
        self.bleCallback = bleCallback
        self.not_found = False

        if self.bleCallback != None:
            from ble_simple_peripheral import bluetooth,BLESimplePeripheral
            from ble_simple_central import BLESimpleCentral
            self.ble = bluetooth.BLE()
            self.blePeripheral = BLESimplePeripheral(self.ble,name=self.bleCallback.bleName)
            self.blePeripheral.on_write(self.bleCallback.didReceiveCallback)
            self.central = BLESimpleCentral(self.ble)

    def isConnected(self):
        if self.bleCallback != None:
            return self.blePeripheral.is_connected()
            
    def isDisconnected(self):
        if self.bleCallback != None:
            return self.blePeripheral.is_disconnected()
        

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

    
    def send(self,data):
        if self.bleCallback != None:
            if self.blePeripheral.is_connected():
                self.blePeripheral.send(data)
                print("Message send:", data)

    def receive(self):
        self.blePeripheral.on_write(self.bleCallback.didReceiveCallback)