i = 0
while i < len(valuesArray):
  if int(valuesArray[i]) >= self.highParam:
    print(int(valuesArray[i]))
    self.sensorsLeds[i][0] = (0, 255, 0)
    self.vibrationMotor.value(0)
    self.sensorsLeds[i].write()

  elif self.lowParam < int(valuesArray[i]) < self.highParam:
    print(int(valuesArray[i]))
    currentLed = 0
    while currentLed < self.nofLeds:
      self.sensorsLeds[i][currentLed] = (255, 0, 0)
      self.vibrationMotor.value(1)
      self.sensorsLeds[i].write()
      currentLed += 1

  else:
    print(int(valuesArray[i]))
    currentLed = 0
    while currentLed < self.nofLeds:
      self.sensorsLeds[i][currentLed] = (0,0,0)
      self.vibrationMotor.value(0)
      currentLed += 1

  print('#####', i, '#####')
  i+=1




[NeoPixel(Pin(27), self.nofLeds),
NeoPixel(Pin(19), self.nofLeds),
NeoPixel(Pin(32), self.nofLeds),
NeoPixel(Pin(23), self.nofLeds),
NeoPixel(Pin(0), self.nofLeds)]
