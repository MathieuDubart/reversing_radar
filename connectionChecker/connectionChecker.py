from connectionStates import *

class BleConnectionChecker:
  def __init__(self,ble):
    self._ble = ble
    self._currentState = BleInitialState()
    self._currentState.context = self
    self.bluetoothConnection = False
  
  def _isConnected(self) -> bool:
    return self._ble.isConnected()
  
  def _updateState(self, newState):
    self._currentState = newState
    self._currentState.context = self

  def _printConnection(self):
    self._currentState.printConnection()

  def _checkBluetoothConnection(self):
    if self._isConnected():
      self._updateState(BleConnectedState())
    else:
      self._updateState(BleNotConnectedState())

    self._printConnection()
    self.bluetoothConnection = self._currentState.connected


class AckChecker:
  def __init__(self, ble):
    self._ble = ble
    self._currentState = BleInitialState()
    self._currentState.context = self
    self.bluetoothConnection = False
        
