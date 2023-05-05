from connectionStates import *
from time import sleep

class BleConnectionChecker:
  def __init__(self,ble, nofTry):
    self._ble = ble
    self._nofTry = nofTry
    self._currentState = BleInitialState()
    self._currentState.context = self
    self.bluetoothConnection = False
    self._currentTry = 0
  
  def _isConnected(self) -> bool:
    return self._ble.isConnected()
  
  def _updateState(self, newState):
    self._currentState = newState
    self._currentState.context = self

  def _printConnection(self):
    self._currentState.printConnection()

  def checkBluetoothConnection(self):

    if self._isConnected():
      self._updateState(BleConnectedState())
    elif self._currentTry <= self._nofTry:
      print("Retrying to connect...")
      self._updateState(BleNotConnectedState())
      self._currentTry = self._currentTry +1
    else:
      self._printConnection()
      print("Error: impossible to connect to bluetooth after {} tries.".format(self._currentTry))

    self._printConnection()
    self.bluetoothConnection = self._currentState.connected


class AckChecker:
  def __init__(self, ble, nofTry):
    self._ble = ble
    self._nofTry = nofTry
    self._currentState = AckInitialState()
    self._currentState.context = self
    self.ackConnection = False

  def _updateState(self, newState):
    self._currentState = newState
    self._currentState.context = self

  def _printConnection(self):
    self._currentState.printConnection()
        
  def _checkAck(self):
    self._ble.send("ack_testing")
    sleep(3)
    ack_bool = self._ble.receive()

    if ack_bool == True:
      self._updateState(AckConnectedState())
    elif self._currentTry <= self._nofTry:
      print("Retrying to connect...")
      self._updateState(AckNotConnectedState())
      self._currentTry = self._currentTry +1
    else:
      print("Error: impossible to verify ACK after {} tries.".format(self._currentTry))
      self._updateState(AckNotConnectedState())

    self._printConnection()
    self.ackConnection = self._currentState.connected


class BleAckChecker:
  def __init__(self, BleChecker, ble, AckChecker, ack, nofTry = 3):
    self._BleChecker = BleChecker(ble, nofTry)
    self._AckChecker = AckChecker(ack, nofTry)
    