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
    self._bluetoothConnection = False
    self._currentTry = 0
  
  def _isConnected(self) -> bool:
    return self._ble.isConnected()
  
  def _updateState(self, newState):
    self._currentState = newState
    self._currentState.context = self

  def printConnection(self):
    self._currentState.printConnection()

  def getConnectionState(self):
    return self._bluetoothConnection

  def checkBluetoothConnection(self):

    if self._isConnected():
      self._updateState(BleConnectedState())
    elif self._currentTry <= self._nofTry:
      print("Retrying to connect...")
      self._updateState(BleNotConnectedState())
      self._currentTry = self._currentTry +1
    else:
      self._updateState(BleNotConnectedState())
      self._printConnection()
      print("Error: impossible to connect to bluetooth after {} tries.".format(self._currentTry))

    self.printConnection()
    self.bluetoothConnection = self._currentState.isConnected()


class AckChecker(ConnectionProtocol):
  def __init__(self, ble, nofTry):
    self._ble = ble
    self._nofTry = nofTry
    self._currentState = AckNotConnectedState()
    self._currentState.context = self
    self._ackConnection = False

  def _updateState(self, newState):
    self._currentState = newState
    self._currentState.context = self

  def printConnection(self):
    self._currentState.printConnection()

  def getConnectionState(self):
    return self._ackConnection
        
  def checkAck(self):
    ack_res = self._ble.receive()
    sleep(3)
    self._ble.send("ack")

    if ack_res == "ack":
      self._updateState(AckConnectedState())
    elif self._currentTry <= self._nofTry:
      print("Retrying to connect...")
      self._updateState(AckNotConnectedState())
      self._currentTry = self._currentTry +1
    else:
      self._updateState(AckNotConnectedState())
      print("Error: impossible to verify ACK after {} tries.".format(self._currentTry))

    self.printConnection()
    self.ackConnection = self._currentState.isConnected()


class BleIsReady:
  def __init__(self, BleChecker, ble, AckChecker, ack, nofTry = 3):
    self._BleChecker = BleChecker(ble, nofTry)
    self._AckChecker = AckChecker(ack, nofTry)
    self.currentState = BleIsNotReady()
    self.currentState.context = self

  def _updateState(self, newState):
    self.currentState = newState
    self.currentState.context = self

  def process(self):
    self._BleChecker.checkBluetoothConnection()
    if self._BleChecker.getConnectionState():
      self._AckChecker.checkAck()
      if self._AckChecker.getConnectionState():
        self._updateState(BleIsReady())
      else: 
        self._AckChecker.printConnection()
    else:
      self._BleChecker.printConnection()
    