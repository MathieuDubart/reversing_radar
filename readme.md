# Reversing radar for electric wheeling chair

### Hardware:
- 6 ultra-sound sensors
- 2 ESP32
- 5 LEDS bands (4 Leds per band)
- 1 vibration motor

### Wiring:

Wires: 1 tape = Vcc || 2 tapes = Gnd
One wire color per sensor

Black wire Breadboard -> ESP: 5v || White wire Breadboard -> ESP: Gnd

Sensors Pins:

1) Trigger: 32 | Echo: 34 -> Violet
2) Trigger: 25 | Echo: 33 -> Orange
3) Trigger: 14 | Echo: 12 -> Red
4) Trigger: 19 | Echo: 18 -> Blue
5) Trigger: 16 | Echo: 4 -> Green
6) Trigger: 15 | Echo: 2 -> Yellow

LEDs Pins:
1) Red: 22 | Green: 15
2) Red: 19 | Green: 18
3) Red: 17 | Green: 4
4) Red: 26 | Green: 14

### ESP32 Config:

- For sensors ESP32:

Put all the files from ```ESP-32-SENSORS``` directory + ```connectionCheckersSensors``` & ```connectionStates``` from ```connectionChecker``` directory.

- For pad ESP32:

Put all the files from ```ESP-32-LEDS```dircetory + ```connectionCheckersPad``` & ```connectionStates``` from ```connectionChecker```directory.