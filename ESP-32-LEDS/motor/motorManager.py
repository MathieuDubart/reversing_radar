from machine import Pin
from motorStates import *
from padStates import *

class MotorManager:
  def __init__(self, motorPin):
    self.motor = Pin(motorPin, Pin.OUT)
    self.currentState = MotorInitialState()
    self.ledsStates = [PadInitialState(),
                      PadInitialState(),
                      PadInitialState(),
                      PadInitialState(),
                      PadInitialState()]

  def __updateState(self, newState):
    if PadSemiNearState or PadNearState in self.ledsStates:
      if str(self.currentState) != str(newState):
        self.currentState = newState
        self.currentState.context = self
        print("New State: ", self.currentState)