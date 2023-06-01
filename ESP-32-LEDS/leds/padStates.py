class PadStates:
  def __init__(self):
    pass

  def __str__(self):
    pass

  def turnOnBand(self):
    pass


class PadInitialState(PadStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Pad Initial State"
    
  def turnOnBand(self):
    currentLed = 0
    while currentLed < self.context.padManager.nofLeds:
      self.context.led[currentLed] = (0, 0, 0)
      print(self.context.led[currentLed])
      currentLed += 1
    self.context.led.write()
    self.context.padManager.vibrationMotor.value(0)


class PadFarState(PadStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Pad Far State"
  
  def turnOnBand(self):
    currentLed = 0
    while currentLed < 1:
      self.context.led[currentLed] = self.context.padManager.ledsColors[currentLed]
      currentLed += 1
    
    while currentLed < self.context.padManager.nofLeds:
      self.context.led[currentLed] = (0, 0, 0)
      currentLed += 1
    self.context.led.write()
    self.context.padManager.vibrationMotor.value(0)


class PadSemiFarState(PadStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Pad Semi Far State"
  
  def turnOnBand(self):
    currentLed = 0
    while currentLed < 2:
      self.context.led[currentLed] = self.context.padManager.ledsColors[currentLed]
      currentLed += 1
    
    while currentLed < self.context.padManager.nofLeds:
      self.context.led[currentLed] = (0, 0, 0)
      currentLed += 1
    self.context.led.write()
    self.context.padManager.vibrationMotor.value(0)


class PadSemiNearState(PadStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Pad Semi Near State"

  def turnOnBand(self):
    currentLed = 0
    while currentLed < 3:
      self.context.led[currentLed] = self.context.padManager.ledsColors[currentLed]
      currentLed += 1
    
    while currentLed < self.context.padManager.nofLeds:
      self.context.led[currentLed] = (0, 0, 0)
      currentLed += 1
    self.context.led.write()
    self.context.padManager.vibrationMotor.value(1)
    

class PadNearState(PadStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Pad Near State"

  def turnOnBand(self):
    currentLed = 0
    while currentLed < 4:
      self.context.led[currentLed] = self.context.padManager.ledsColors[currentLed]
      currentLed += 1
    
    while currentLed < self.context.padManager.nofLeds:
      self.context.led[currentLed] = (0, 0, 0)
      currentLed += 1
    self.context.led.write()
    self.context.padManager.vibrationMotor.value(1)


class PadOutOfRangeState(PadStates):
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
    self.context.padManager.vibrationMotor.value(0)