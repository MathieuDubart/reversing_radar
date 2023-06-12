from time import sleep_ms

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
    pass

class MotorOffState(MotorStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Motor Off States"
  
  def turnOnMotor(self):
    self.context.motor.value(0)

class MotorSlowState(MotorStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Motor Slow States"
  
  def turnOnMotor(self):
    self.context.motor.value(1)
    sleep_ms(1500)
    self.context.motor.value(0)
    sleep_ms(1500)

class MotorSemiSlowState(MotorStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Motor Semi Slow States"
  
  def turnOnMotor(self):
    self.context.motor.value(1)
    sleep_ms(1000)
    self.context.motor.value(0)
    sleep_ms(1000)

class MotorSemiFastState(MotorStates):
  def __init__(self):
    super().__init__()

  def __str__(self):
    return "Motor Semi Fast States"
  
  def turnOnMotor(self):
    self.context.motor.value(1)
    sleep_ms(500)
    self.context.motor.value(0)
    sleep_ms(500)

class MotorFastState(MotorStates):
  def __init__(self):
    pass

  def __str__(self):
    return "Motor Fast State"
  
  def turnOnMotor(self):
    self.context.motor.value(1)
