class ConnectionState:
  def __init__(self):
    self.connected = False
  
  def isConnected(self):
    return self.connected
  
  def printConnection(self):
    pass

class BleConnectedState(ConnectionState):
  def __init__(self):
    self.connected = True
  
  def isConnected(self):
    return self.connected

  def printConnection(self):
    print('Bluetooth connection established')

class BleNotConnectedState(ConnectionState):
  def __init__(self):
    super().__init__()
  
  def isConnected(self):
    return self.connected
  
  def printConnection(self):
    print('Unable to connect to bluetooth')

class AckConnectedState(ConnectionState):
  def __init__(self):
    self.connected = True
  
  def isConnected(self):
    return self.connected
  
  def printConnection(self):
    print('Ack verified')

class AwaitingAck(ConnectionState):
  def __init__(self):
    super().__init__()
  
  def isConnected(self):
    return self.connected
  
  def printConnection(self):
    print('Awaiting Ack...')


class AckNotConnectedState(ConnectionState):
  def __init__(self):
    super().__init__()
  
  def isConnected(self):
    return self.connected
  
  def printConnection(self):
    print('Unable to verify Ack')

class BleIsReady(ConnectionState):
  def __init__(self):
    self.connected = True

  def isConnected(self):
    return self.connected
    
  def printConnection(self):
    print('Ble is ready')
  
class BleIsNotReady(ConnectionState):
  def __init__(self):
    super().__init__()

  def isConnected(self):
    return self.connected
  
  def printConnection(self):
    print('Ble is not ready')
