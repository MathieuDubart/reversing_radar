from sensorsStates import *

class SensorManager:
  def __init__(self, value, redLed, greenLed, lowParam = 2, highParam = 40):
    self.value = value
    self.lowParam = lowParam
    self.highParam = highParam
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
    if self.value > self.highParam:
      self.__updateState(FarState())
      self.currentState.turnOnLeds(self.redLed, self.greenLed)


    elif self.lowParam < self.value =< self.highParam:
      self.__updateState(NearState())
      self.currentState.turnOnLeds(self.redLed, self.greenLed)

    else:
      self.__updateState(InitialState())
      self.currentState.turnOnLeds(self.redLed, self.greenLed)

  def process(self):
    print("Current State: ", self.currentState)
    self.__stateChecking()