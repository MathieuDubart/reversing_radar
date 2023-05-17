class padStates:
  def __init__(self):
    pass

  def __throughArray(self, minusLeds):
    pass

  def turnOnPad(self, ledsArray, index, valuesArray, minusLeds):
    pass


class InitialState(padStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
      return "Initial State"
    
  def turnOnPad(self, ledsArray, valuesArray, minusLeds):
    currentLed = 0
    while currentLed < self.nofLeds:
      ledsArray[self.context.i][currentLed] = (255, 0, 0)
      self.vibrationMotor.value(1)
      ledsArray[self.context.i].write()
      currentLed += 1


class FarState(padStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Far State"
  
  def turnOnPad(self, ledsArray, index, valuesArray, minusLeds):
    currentLed = 0
    while currentLed < self.nofLeds:
      ledsArray[index][currentLed] = (0, 0, 255)
      self.vibrationMotor.value(1)
      ledsArray[index].write()
      currentLed += 1


class SemiFarState(padStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Semi Far State"
  
  def turnOnPad(self, ledsArray, index, valuesArray, minusLeds):
    currentLed = 0
    while currentLed < self.nofLeds:
      ledsArray[index][currentLed] = (0, 255, 0)
      self.vibrationMotor.value(1)
      ledsArray[index].write()
      currentLed += 1


class SemiNearState(padStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Semi Near State"

  def turnOnPad(self, ledsArray, index, valuesArray, minusLeds):
    currentLed = 0
    while currentLed < self.nofLeds:
      ledsArray[index][currentLed] = (255, 255, 0)
      self.vibrationMotor.value(1)
      ledsArray[index].write()
      currentLed += 1
    

class NearState(padStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Near State"

  def turnOnPad(self, ledsArray, index, valuesArray, minusLeds):
    currentLed = 0
    while currentLed < self.nofLeds:
      ledsArray[index][currentLed] = (255, 0, 255)
      self.vibrationMotor.value(1)
      ledsArray[index].write()
      currentLed += 1


class OutOfRangeState(padStates):
  def __init__(self):
    super().__init__()
  
  def __str__(self):
    return "Out of Range State"
  
  def turnOnPad(self, ledsArray, index, valuesArray, minusLeds):
    self.redLed.value(0)
    self.greenLed.value(0)
  