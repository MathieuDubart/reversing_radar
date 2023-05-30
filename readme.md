# Reversing radar for electric wheeling chair

### Hardware:
- 6 ultra-sound sensors
- 2 ESP32
- 5 LEDS bands (4 Leds per band)
- 1 vibration motor

### Wiring:

## Common: 
Wires: 1 tape = Vcc || 2 tapes = Gnd
One wire color per sensor

Black wire Breadboard -> ESP: 5v || White wire Breadboard -> ESP: Gnd

## Sensors Pins:
1) Trigger: 32 | Echo: 34 -> Violet wires
2) Trigger: 25 | Echo: 33 -> Orange wires
3) Trigger: 14 | Echo: 12 -> Red wires
4) Trigger: 19 | Echo: 18 -> Blue wires
5) Trigger: 16 | Echo: 4 -> Green wires
6) Trigger: 15 | Echo: 2 -> Yellow wires

## LEDs Pins:
1) Din: 27
2) Din: 19
3) Din: 32
4) Din: 23
5) Din: 0

### ESP32 Config:
- For sensors ESP32:

Put all the files from ```ESP-32-SENSORS``` directory + ```connectionCheckersSensors``` & ```connectionStates``` from ```connectionChecker``` directory.

- For pad ESP32:

Put all the files from ```ESP-32-LEDS```dircetory + ```connectionCheckersPad``` & ```connectionStates``` from ```connectionChecker```directory.