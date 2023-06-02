from padStates import *
from ledManager import *
from motorManager import *
from motorStates import *

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
    self.vibrationMotor = MotorManager(motorPin = 26)
    self.ledsColors = [(0, 255, 0), (255, 204, 0), (255, 70, 0), (255, 0, 0)]

  def __stateManagement(self, newStateSensors, index, newStateMotor):
    self.sensorsLeds[index].__updateState(newStateSensors)

    self.vibrationMotor.ledsStates[index] = type(self.sensorsLeds[index].currentState)
    self.vibrationMotor.__updateState(newStateMotor)

    self.sensorsLeds[index].currentState.turnOnBand()
    self.vibrationMotor.turnOnMotor()

  def __stateChecking(self, valuesArray):
    i = 0
    while i < len(valuesArray):
      if int(valuesArray[i]) >= self.highParam:
        self.__stateManagement(PadFarState(), i, MotorFarState())
        print(int(valuesArray[i]),':',self.sensorsLeds[i].currentState)

      elif self.lowParam*1.25 < int(valuesArray[i]) < self.highParam:
        self.__stateManagement(PadSemiFarState(), i, MotorFarState())
        print(int(valuesArray[i]),':',self.sensorsLeds[i].currentState)

      elif self.lowParam/2 < int(valuesArray[i]) < self.lowParam*1.25:
        self.__stateManagement(PadSemiNearState(), i, MotorNearState())
        print(int(valuesArray[i]),':',self.sensorsLeds[i].currentState)

      elif 0 < int(valuesArray[i]) < self.lowParam/2:
        self.__stateManagement(PadNearState(), i, MotorNearState())
        print(int(valuesArray[i]),':',self.sensorsLeds[i].currentState)

      else:
        self.__stateManagement(PadOutOfRangeState(), i, MotorOutOfRangeState())
        print(int(valuesArray[i]),':',self.sensorsLeds[i].currentState)

      i+=1  
    print('##### DEBUG', self.vibrationMotor.ledsStates)
    print ('##########################')
  def delegate(self, valuesArray):
    self.__stateChecking(valuesArray = valuesArray)