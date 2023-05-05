class ConnectionState:
  def __init__(self):
    self.connected = False

  def printConnection():
    pass

class BleInitialState(ConnectionState):
  def __init__(self):
    super().__init__()

  def printConnection():
    print('Connecting to bluetooth...')

class BleConnectedState(ConnectionState):
  def __init__(self):
    self.connected = True
  
  def printConnection():
    print('Bluetooth connection established')

class BleNotConnectedState(ConnectionState):
  def __init__(self):
    super().__init__()
  
  def printConnection():
    print('Unable to connect to bluetooth')

class AckInitialState(ConnectionState):
  def __init__(self):
    super().__init__()

  def printConnection():
    print('Checking ACK...')

class AckConnectedState(ConnectionState):
  def __init__(self):
    self.connected = True
  
  def printConnection():
    print('Ack verified')

class AckNotConnectedState(ConnectionState):
  def __init__(self):
    super().__init__()
  
  def printConnection():
    print('Unable to verify Ack')
