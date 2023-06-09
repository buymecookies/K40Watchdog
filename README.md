This repository is under construction early beta stuff.

# K40Watchdog
k40 laser watchdog for picopi w 

Functions to build 

- Lcd screen with rotary encoder.
- buzzer
- Flow meter yf-s201 with 
- in + flow out detection
- Lid protection ( front, rear, psu)
- 3x temp sensor (in, ou , basin)
- Laser enable output to k40 psu
- Air assist solenoid control
- compressor power control
- Fume removal control
- waterflow control


## i2c
| Status          | Name                    | Gpio  | gpio type        | hardware                   |
|-----------------|-------------------------|------:|------------------|----------------------------|
| Breadboard done | lcd screen              |     0 | i2c sda          | 20x4 i2c lcd screen        |
| Breadboard done | lcd screen              |     1 | i2c scl          | 20x4 i2c lcd screen        |
|                 |                         |       |                  |                            |

## inputs
| Status          | Name                    | Gpio  | gpio type        | Hardware                   |
|-----------------|-------------------------|------:|------------------|----------------------------|
| Breadboard done | rotary encoder switch   |     2 | digital input    | Rotary encoder module      |
| Breadboard done | rotary encoder knob     |   3&4 | 2x digital input | Rotary encoder module      |
|                 | Lid front               |     5 | input            | endstop switch             |
|                 | Lid back                |     6 | input            | endstop switch             |
|                 | Lid psu                 |     7 | input            | endstop switch             |
|                 | waterflow out           |     8 | input            | Waterflow on off switch    |
|                 | start cooldown          |     9 | input            | on/off switch              |
|                 | standby for laser       |    10 | input            | on/off switch              |
|                 | Lid override            |    11 | input            | on/off switch              |
| Breadboard done | waterflow in + liters   |    21 | input            | waterflow sensor           |


## outputs
| Status          | Name                    | Gpio  | gpio type        | hardware                   |
|-----------------|-------------------------|------:|------------------|----------------------------|
|                 | Laser enable            |    13 | Digital output   | dry contact                |
|                 | 230v compressor         |    14 | Digital output   | 230v control               |
|                 | Air assist              |    15 | Digital output   | solenoid                   |
|                 | air suction   m         |    16 | Digital output   | 230v control               |
|                 | Waterpump cooling       |    17 | Digital output   | 230v control               |
|                 | waterpump tube          |    18 | Digital output   | 230v control               |
|                 | water flow switch a-b   |    19 | Digital output   | relay 12v                  |
|                 | Cooling on              |    20 | Digital output   | dry contact                |
|                 | buzzer                  |    22 | Digital output   | piezo buzzer               |

## ADC
| Status          | Name                    | Gpio  | gpio type        | hardware                   |
|-----------------|-------------------------|------:|------------------|----------------------------|
|                 | Temprature basin        |    26 | adc              | thermistor                 |
|                 | Temprature laser input  |    27 | adc              | thermistor                 |
|                 | Temprature laser output |    28 | adc              | thermistor                 |
