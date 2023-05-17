class PadStates:
  def __init__(self):
    pass

  def turnOnBand(self, minusLeds):
    pass

# RESTE: ALLUMER LES BONNES LEDS DE LA BONNE COULEUR

class InitialState(PadStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Initial State"
    
  def turnOnBand(self, minusLeds):
    currentLed = 0
    while currentLed < self.context.padManager.nofLeds:
      self.context.led[currentLed] = (0, 0, 0)
      print(self.context.led[currentLed])
      self.context.led.write()
      currentLed += 1


class FarState(PadStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Far State"
  
  def turnOnBand(self, minusLeds):
    currentLed = 0
    while currentLed < self.context.padManager.nofLeds:
      self.context.led[currentLed] = (0, 255, 0)
      print(self.context.led[currentLed])
      self.context.led.write()
      currentLed += 1


class SemiFarState(PadStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Semi Far State"
  
  def turnOnBand(self, minusLeds):
    currentLed = 0
    while currentLed < self.context.padManager.nofLeds:
      self.context.led[currentLed] = (255, 234, 0)
      print(self.context.led[currentLed])
      self.context.led.write()
      currentLed += 1


class SemiNearState(PadStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Semi Near State"

  def turnOnBand(self, minusLeds):
    currentLed = 0
    while currentLed < self.context.padManager.nofLeds:
      self.context.led[currentLed] = (255, 155, 0)
      print(self.context.led[currentLed])
      self.context.led.write()
      currentLed += 1
    

class NearState(PadStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Near State"

  def turnOnBand(self, minusLeds):
    currentLed = 0
    while currentLed < self.context.padManager.nofLeds:
      self.context.led[currentLed] = (255, 0, 0)
      print(self.context.led[currentLed])
      self.context.led.write()
      currentLed += 1

class OutOfRangeState(PadStates):
  def __init__(self):
    super().__init__()
  
  def __str__(self):
    return "Out of Range State"
  
  def turnOnBand(self, minusLeds):
    currentLed = 0
    while currentLed < self.context.padManager.nofLeds:
      self.context.led[currentLed] = (0, 0, 0)
      print(self.context.led[currentLed])
      self.context.led.write()
      currentLed += 1
  