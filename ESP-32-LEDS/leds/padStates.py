class PadStates:
  def __init__(self):
    pass

  def turnOnBand(self):
    pass


class InitialState(PadStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Initial State"
    
  def turnOnBand(self):
    currentLed = 0
    while currentLed < self.context.padManager.nofLeds:
      self.context.led[currentLed] = (0, 0, 0)
      print(self.context.led[currentLed])
      currentLed += 1
    self.context.led.write()


class FarState(PadStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Far State"
  
  def turnOnBand(self):
    currentLed = 0
    while currentLed < 1:
      self.context.led[currentLed] = self.context.padManager.ledsColors[currentLed]
      currentLed += 1
    
    while currentLed < self.context.padManager.nofLeds:
      self.context.led[currentLed] = (0, 0, 0)
      currentLed += 1
    self.context.led.write()

class SemiFarState(PadStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Semi Far State"
  
  def turnOnBand(self):
    currentLed = 0
    while currentLed < 2:
      self.context.led[currentLed] = self.context.padManager.ledsColors[currentLed]
      currentLed += 1
    
    while currentLed < self.context.padManager.nofLeds:
      self.context.led[currentLed] = (0, 0, 0)
      currentLed += 1
    self.context.led.write()



class SemiNearState(PadStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Semi Near State"

  def turnOnBand(self):
    currentLed = 0
    while currentLed < 3:
      self.context.led[currentLed] = self.context.padManager.ledsColors[currentLed]
      currentLed += 1
    
    while currentLed < self.context.padManager.nofLeds:
      self.context.led[currentLed] = (0, 0, 0)
      currentLed += 1
    self.context.led.write()
    

class NearState(PadStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Near State"

  def turnOnBand(self):
    currentLed = 0
    while currentLed < 4:
      self.context.led[currentLed] = self.context.padManager.ledsColors[currentLed]
      currentLed += 1
    
    while currentLed < self.context.padManager.nofLeds:
      self.context.led[currentLed] = (0, 0, 0)
      currentLed += 1
    self.context.led.write()

class OutOfRangeState(PadStates):
  def __init__(self):
    super().__init__()
  
  def __str__(self):
    return "Out of Range State"
  
  def turnOnBand(self):
    currentLed = 0
    while currentLed < self.context.padManager.nofLeds:
      self.context.led[currentLed] = (0, 255, 0)
      print(self.context.led[currentLed])
      currentLed += 1
    self.context.led.write()