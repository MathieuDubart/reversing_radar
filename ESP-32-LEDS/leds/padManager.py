from padStates import *
from machine import Pin
from neopixel import NeoPixel

class padManager:
  def __init__(self,lowParam, highParam, nofLeds):
    self.lowParam = lowParam
    self.highParam = highParam
    self.sensorsLeds = [NeoPixel(Pin(27), self.nofLeds),
                        NeoPixel(Pin(19), self.nofLeds),
                        NeoPixel(Pin(32), self.nofLeds),
                        NeoPixel(Pin(23), self.nofLeds),
                        NeoPixel(Pin(0), self.nofLeds)]
    self.nofLeds = nofLeds
    self.vibrationMotor = Pin(26, Pin.OUT)
    self.currentState = InitialState()
    self.currentState.context = self

  def __stateManagement(self, newState, valuesArray, minusLeds = 0):
    self.__updateState(newState)
    self.currentState.turnOnPad(ledsArray = self.sensorsLeds, valuesArray = valuesArray, minusLeds = minusLeds)

  def __updateState(self, newState):
    if str(self.currentState) != str(newState):
      self.currentState = newState
      self.currentState.context = self
      print("New State: ", self.currentState)
  
  def __stateChecking(self, valuesArray):
    i = 0
    while i < len(valuesArray):
      if int(valuesArray[i]) >= self.highParam:
        print(int(valuesArray[i]))
        self.__updateState(FarState())
        self.currentState.turnOnPad(ledsArray = self.sensorsLeds, index = i, valuesArray = valuesArray)

      elif self.lowParam*2 < int(valuesArray[i]) < self.highParam/2:
        print(int(valuesArray[i]))
        self.__stateManagement(self, SemiFarState(), valuesArray, 3)

      elif self.lowParam < int(valuesArray[i]) < self.lowParam*2:
        print(int(valuesArray[i]))
        self.__stateManagement(self, SemiNearState(), valuesArray, 2)

      elif 0 < int(valuesArray[i]) < self.lowParam:
        print(int(valuesArray[i]))
        self.__stateManagement(self, NearState(), valuesArray, 1)

      else:
        print(int(valuesArray[i]))
        self.__stateManagement(self, OutOfRangeState, valuesArray)

      print('#####', i, '#####')
      i+=1  
    
  def delegate(self, valuesArray):
    print("Current State: ", self.currentState)
    self.__stateChecking(valuesArray = valuesArray)