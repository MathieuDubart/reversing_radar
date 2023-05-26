from connectionStates import *
from time import sleep

class ConnectionProtocol:
  def __init__(self):
    pass

  def _updateState(self, newState):
    pass

  def printConnection(self):
    pass

  def getConnection(self):
    pass


class BleConnectionChecker(ConnectionProtocol):
  def __init__(self,wirelessManager, nofTry):
    self._ble = wirelessManager
    self._nofTry = nofTry
    self._currentState = BleNotConnectedState()
    self._currentState.context = self
    self._currentTry = 0
  
  def _isConnected(self) -> bool:
    return self._ble.isConnected()
  
  def _updateState(self, newState):
    self._currentState = newState
    self._currentState.context = self

  def printConnection(self):
    self._currentState.printConnection()

  def getCurrentState(self):

    if type(self._currentState) == BleConnectedState:
      return True
    else:
      return False

  def checkBluetoothConnection(self):

    if self._isConnected():
      self._updateState(BleConnectedState())
    elif self._nofTry > self._currentTry:
      print("Retrying to connect in 3s...")
      sleep(3)
      self._updateState(BleNotConnectedState())
      self._currentTry = self._currentTry +1
      self.checkBluetoothConnection()
    else:
      self._updateState(BleNotConnectedState())
      print("Error: impossible to connect to bluetooth after {} tries.".format(self._currentTry))

    self.printConnection()


class AckChecker(ConnectionProtocol):
  def __init__(self, wirelessManager, nofTry):
    self._ble = wirelessManager
    self._nofTry = nofTry
    self._currentState = AckNotConnectedState()
    self._currentState.context = self
    self._ackConnection = False
    self._currentTry = 0

  def _updateState(self, newState):
    self._currentState = newState
    self._currentState.context = self

  def printConnection(self):
    self._currentState.printConnection()

  def getCurrentState(self):
    if type(self._currentState) == AckConnectedState:
      return True
    else:
      return False
        
  def checkAck(self):
    self._ble.send("ack-radar")
    self._updateState(AckConnectedState())
    ack_res = self._ble.receive()
    if ack_res == "ack-radar":
      self._updateState(AckConnectedState())
    elif self._nofTry > self._currentTry-1:
      print("Retrying ACK in 3s...")
      sleep(3)
      self._updateState(AckNotConnectedState())
      self._currentTry = self._currentTry +1
      self.checkAck()
    else:
      self._updateState(AckNotConnectedState())
      print("Error: impossible to verify ACK after {} tries.".format(self._currentTry))

    self.printConnection()
    self._ackConnection = self._currentState.isConnected()


class BleStateManager:
  def __init__(self, bleChecker, ackChecker, wirelessManager, nofTry = 3):
    self._BleChecker = bleChecker(wirelessManager, nofTry)
    self._AckChecker = ackChecker(wirelessManager, nofTry)
    self.currentState = BleIsNotReady()
    self.currentState.context = self

  def _updateState(self, newState):
    self.currentState = newState
    self.currentState.context = self

  def process(self):
    self._BleChecker._ble.connect()
    self._BleChecker.checkBluetoothConnection()
    if self._BleChecker.getCurrentState():
      self._AckChecker.checkAck()
      if self._AckChecker.getCurrentState():
        self._updateState(BleIsReady())
      else: 
        self._updateState(BleIsNotReady())
        self._AckChecker.printConnection()
    else:
      self._updateState(BleIsNotReady())
      self._BleChecker.printConnection()
    
