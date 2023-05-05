class SensorsStates:
  def __init__(self):
    pass

  def turnOnLeds(self, redLed, greenLed):
    pass


class InitialState(SensorsStates):
  def __init__(self):
    pass

  def __str__(self):
      return "initialstate"
    
  def turnOnLeds(self, redLed, greenLed):
    self.redLed.value(0)
    self.greenLed.value(0)
  

class FarState(SensorsStates):
  def __init__(self):
    pass

  def __str__(self):
    return "farstate"
  
  def turnOnLeds(self, redLed, greenLed):
    self.redLed.value(0)
    self.greenLed.value(1)


class NearState(SensorsStates):
  def __init__(self):
    pass

  def __str__(self):
    return "nearstate"

  def turnOnLeds(self, redLed, greenLed):
    self.redLed.value(1)
    self.greenLed.value(0)