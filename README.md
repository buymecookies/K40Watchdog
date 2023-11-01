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

| Breadboard done | Lid front               |   enable  5 | input            | endstop switch             |
| Breadboard done | Lid back                |     6 | input            | endstop switch             |
| Breadboard done | Lid psu                 |     7 | input            | endstop switch             |
| Breadboard done | Lid override            |     8 | input            | on/off switch              |

| Breadboard done | prepare                 |     9 | input            | on/off switch              |
| Breadboard done | start lasering          |    10 | input            | on/off switch              |

| Breadboard done | waterflow in + liters   |    21 | input            | waterflow sensor           |


## outputs
| Status          | Name                    | Gpio  | gpio type        | object                     |
|-----------------|-------------------------|------:|------------------|----------------------------|
| Breadboard done | Laser enable            |    13 | Digital output   | enable                     |
| Breadboard done | 230v compressor         |    14 | Digital output   | comp230v                   |
| Breadboard done | chiller on              |    15 | Digital output   | chiller                    |
| Breadboard done | Waterpump cooling       |    16 | Digital output   | coolPump                   |
| Breadboard done | ventilation             |    17 | Digital output   | vent                       |
| Breadboard done | waterpump laser tube    |    18 | Digital output   | tubePump                   |
| Breadboard done | Air assist              |    19 | Digital output   | airAss                     |


## ADC
| Status          | Name                    | Gpio  | gpio type        | hardware                   |
|-----------------|-------------------------|------:|------------------|----------------------------|
|                 | Temprature basin        |    26 | adc              | thermistor                 |
|                 | Temprature laser input  |    27 | adc              | thermistor                 |
|                 | Temprature laser output |    28 | adc              | thermistor                 |
