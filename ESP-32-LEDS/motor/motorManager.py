from machine import Pin
from motorStates import *
from padStates import *

class MotorManager:
  def __init__(self, motorPin):
    self.motor = Pin(motorPin, Pin.OUT)
    self.currentState = MotorInitialState()
    self.ledsStates = [PadInitialState,
                      PadInitialState,
                      PadInitialState,
                      PadInitialState,
                      PadInitialState]

  # Pas besoins du param newState
  def __updateState(self):
    #boucle for de  ledstates
    # tu compte le nombre d'état différent de semi near ou near (tu l'app numberOfInactiveState)

    # si ce nb est de ledstats.lenght (5) alors aucun des leds est dans un etat qui 
    # necessite la vibration donc currentState = motorFarState

    # sinon si numberOfInactiveState est < 5 alors
    # tu mets currentState à motorNearState


    if type(self.currentState) != type():
      self.currentState = 
      self.currentState.context = self
      print("New State: ", self.currentState)
        
  def turnOnMotor(self):
    self.currentState.turnOnMotor()