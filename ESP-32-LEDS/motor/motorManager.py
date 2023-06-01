from machine import Pin
from motorStates import *

class MotorManager:
  def __init__(self, motorPin):
    self.motor = Pin(motorPin, Pin.OUT)
    self.currentState = MotorInitialState()

  def __updateState(self, newState):
    if str(self.currentState) != str(newState):
      self.currentState = newState
      self.currentState.context = self
      print("New State: ", self.currentState)