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
  def __init__(self,ble, nofTry):
    self._bleCallback = ble
    self._nofTry = nofTry
    self._currentState = BleNotConnectedState()
    self._currentState.context = self
    self._currentTry = 0
  
  def _isConnected(self) -> bool:
    return self._bleCallback.isConnected()
  
  def _updateState(self, newState):
    self._currentState = newState
    self._currentState.context = self

  def printConnection(self):
    self._currentState.printConnection()

  def getCurrentState(self):
    return self._currentState

  def checkBluetoothConnection(self):

    if self._isConnected():
      self._updateState(BleConnectedState())
    elif self._nofTry-1 > self._currentTry:
      print("Retrying to connect in 3s...")
      sleep(3)
      self._updateState(BleNotConnectedState())
      self._currentTry = self._currentTry +1
      self.checkBluetoothConnection()
    else:
      self._updateState(BleNotConnectedState())
      self.printConnection()
      print("Error: impossible to connect to bluetooth after {} tries.".format(self._currentTry))

    self.printConnection()


class BleStateManager:
  def __init__(self, BleChecker, nofTry = 3):
    self._BleChecker = BleChecker(nofTry)
    self.currentState = BleIsNotReady()
    self.currentState.context = self

  def _updateState(self, newState):
    self.currentState = newState
    self.currentState.context = self

  def process(self):
    self._BleChecker.checkBluetoothConnection()
    if type(self._BleChecker.getCurrentState()) == BleConnectedState:
      self._updateState(BleIsReady())
    else:
      self._BleChecker.printConnection()
    
