from padStates import *
from machine import Pin
from ledManager import *

class PadManager:
  def __init__(self, lowParam, highParam, nofLeds):
    self.lowParam = lowParam
    self.highParam = highParam
    self.nofLeds = nofLeds
    self.sensorsLeds = [LedManager(27, self),
                        LedManager(19, self),
                        LedManager(32, self),
                        LedManager(23, self),
                        LedManager(0, self)]
    self.vibrationMotor = Pin(26, Pin.OUT)
    self.ledsColors = [(0, 255, 0), (255, 204, 0), (255, 70, 0), (255, 0, 0)]

  def __stateManagement(self, newState, index):
    self.sensorsLeds[index].__updateState(newState)
    self.sensorsLeds[index].currentState.turnOnBand()
  
  def __stateChecking(self, valuesArray):
    i = 0
    while i < len(valuesArray):
      if int(valuesArray[i]) >= self.highParam:
        self.__stateManagement(FarState(), index = i)
        print(int(valuesArray[i]),':',self.sensorsLeds[i].currentState)

      elif self.lowParam*1.25 < int(valuesArray[i]) < self.highParam:
        self.__stateManagement(SemiFarState(), index = i)
        print(int(valuesArray[i]),':',self.sensorsLeds[i].currentState)

      elif self.lowParam/2 < int(valuesArray[i]) < self.lowParam*1.25:
        self.__stateManagement(SemiNearState(), index = i)
        print(int(valuesArray[i]),':',self.sensorsLeds[i].currentState)

      elif 0 < int(valuesArray[i]) < self.lowParam/2:
        self.__stateManagement(NearState(), index = i)
        print(int(valuesArray[i]),':',self.sensorsLeds[i].currentState)

      else:
        self.__stateManagement(OutOfRangeState(), index = i)
        print(int(valuesArray[i]),':',self.sensorsLeds[i].currentState)

      i+=1  
    print ('##########################')
  def delegate(self, valuesArray):
    self.__stateChecking(valuesArray = valuesArray)