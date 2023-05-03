from sensorsStates import *

class SensorManager:
  def __init__(self, sensor, redLed, greenLed):
    self.sensor = sensor
    self.redLed = redLed
    self.greenLed = greenLed
    self.currentState = InitialState()
    self.currentState.context = self

  def __updateState(self, newState):
    if str(self.currentState) != str(newState):
      self.currentState = newState
      self.currentState.context = self
      print("New State: ", self.currentState)
  
  def __stateChecking(self):
    if self.currentState.getDistance() >= 40.0:
      self.redLed.value(0)
      self.greenLed.value(1)
      self.__updateState(FarState())


    elif 2.0 < self.currentState.getDistance() < 40.0:
      self.redLed.value(1)
      self.greenLed.value(0)
      self.__updateState(NearState())

    else:
      self.redLed.value(0)
      self.greenLed.value(0)
      self.__updateState(InitialState())

  def estimateDistance(self):
    print("Current State: ", self.currentState)
    self.__stateChecking()