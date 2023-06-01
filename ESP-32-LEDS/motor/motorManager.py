from machine import PWM
from motorStates import *
from padStates import *

class MotorManager:
  def __init__(self, motorPin):
    self.motor = PWM(motorPin, 1024)
    self.currentState = MotorInitialState()

  def __updateState(self, newState):
    if PadSemiNearState or PadNearState in self.ledsStates:
      if str(self.currentState) != str(newState):
        self.currentState = newState
        self.currentState.context = self
        print("New State: ", self.currentState)