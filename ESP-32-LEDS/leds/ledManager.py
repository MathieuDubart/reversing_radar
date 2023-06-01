from neopixel import NeoPixel
from machine import Pin
from padStates import PadInitialState


class LedManager:
  def __init__(self, ledPin, PadManager):
    self.padManager = PadManager
    self.led = NeoPixel(Pin(ledPin), self.padManager.nofLeds)
    self.currentState = PadInitialState()

  def __updateState(self, newState):
    if str(self.currentState) != str(newState):
      self.currentState = newState
      self.currentState.context = self
      print("New State: ", self.currentState)