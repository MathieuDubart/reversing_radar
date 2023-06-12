from machine import Pin
from motorStates import *
from padStates import *

class MotorManager:
  def __init__(self, motorPin):
    self.motor = Pin(motorPin, Pin.OUT)
    self.currentState = MotorInitialState()
    self.ledsStates = [PadInitialState,
                      PadInitialState,
                      PadInitialState,
                      PadInitialState,
                      PadInitialState]

  def __getNumberOfNearStateLeds(self):
    nofNearStates = 0
    for state in self.ledsStates:
      if state == PadSemiNearState or state == PadNearState:
        nofNearStates += 1

    print("Number of near states:", nofNearStates)
    return nofNearStates


  def __updateState(self):
    if self.__getNumberOfNearStateLeds() == 0:
      self.currentState = MotorOffState()
      self.currentState.context = self
    elif self.__getNumberOfNearStateLeds() == 1:
      self.currentState = MotorSlowState()
      self.currentState.context = self
    elif self.__getNumberOfNearStateLeds() == 2:
      self.currentState = MotorSemiSlowState()
      self.currentState.context = self
    elif self.__getNumberOfNearStateLeds() == 3:
      self.currentState = MotorSemiFastState()
      self.currentState.context = self
    else:
      self.currentState = MotorFastState()
      self.currentState.context = self
    print('Current State:', self.currentState)

  def turnOnMotor(self):
    self.currentState.turnOnMotor()