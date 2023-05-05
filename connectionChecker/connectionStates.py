class ConnectionState:
  def __init__(self):
    pass

  def printConnection():
    pass

class BleInitialState(ConnectionState):
  def __init__(self):
    super().__init__()

  def printConnection():
    print('Connecting to bluetooth...')

class BleConnectedState(ConnectionState):
  def __init__(self):
    super().__init__()
  
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