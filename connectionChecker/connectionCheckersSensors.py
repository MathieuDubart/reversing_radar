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
    self._ble = ble
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


class AckChecker(ConnectionProtocol):
  def __init__(self, ble, nofTry):
    self._ble = ble
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
    return self._currentState
        
  def checkAck(self):
    self._ble.send("ack")
    self._updateState(AwaitingAck())
    sleep(3)
    ack_res = "toto"
    if ack_res == "ack":
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
    self.ackConnection = self._currentState.isConnected()


class BleStateManager:
  def __init__(self, BleChecker, AckChecker, wirelessManager, nofTry = 3):
    self._BleChecker = BleChecker(wirelessManager, nofTry)
    self._AckChecker = AckChecker(wirelessManager, nofTry)
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
    