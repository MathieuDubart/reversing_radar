class MotorStates():
  def __init__(self):
    pass

  def __str__(self):
    pass

  def turnOnMotor(self):
    pass


class MotorInitialState(MotorStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Motor Initial State"
  
  def turnOnMotor(self):
    self.context.motor.value(0)

class MotorFarState(MotorStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Motor Far States"
  
  def turnOnMotor(self):
    self.context.motor.value(0)

class MotorNearState(MotorStates):
  def __init__(self):
    pass

  def __str__(self):
    return "Motor Near State"
  
  def turnOnMotor(self):
    self.context.motor.value(1)