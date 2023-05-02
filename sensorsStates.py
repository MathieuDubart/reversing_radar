class SensorsStates:
  def __init__(self):
    pass

  def getDistance(self):
    pass


class InitialState(SensorsStates):
  def __init__(self):
    pass

  def __str__(self):
      return "initialstate"
    
  def getDistance(self):
    return self.context.sensor.getDistance()
  

class FarState(SensorsStates):
  def __init__(self):
    pass

  def __str__(self):
    return "farstate"
  
  def getDistance(self):
    return self.context.sensor.getDistance()


class NearState(SensorsStates):
  def __init__(self):
    pass

  def __str__(self):
    return "nearstate"

  def getDistance(self):
    return self.context.sensor.getDistance()