# K40Watchdog
PIco PI W K40 laser watchdog

- Functions - 

- Lcd screen with rotary encoder.
- Flow meter in + flow out detection
- Lid protection ( front, rear, psu)
- 3x temp sensor (in, ou , basin)
- Laser enable output to k40 psu
- Air assist solenoid control
- compressor power control
- Fume removal control
- waterflow control

## Inputs
| Status      | Name                    | gpio type        | Hardware                   |
|-------------|-------------------------|------------------|----------------------------|
|             | Lid front               | input            | endstop switch             |
|             | Lid back                | input            | endstop switch             |
|             | Lid psu                 | input            | endstop switch             |
|             | waterflow out           | input            | Waterflow on off switch    |
|             | start cooldown          | input            | on/off switch              |
|             | standby for laser       | input            | on/off switch              |
|             | Lid override            | input            | on/off switch              |
| HW done     | rotary encoder switch   | digital input    | Rotary encoder module      |
| HW done     | rotary encoder knob     | 2x digital input | Rotary encoder module      |
| HW done     | waterflow in + liters   | input            | waterflow sensor           |

## ADC
| Status      | Name                    | gpio type        | Kind of hardware           |
|-------------|-------------------------|------------------|----------------------------|
|             | Temprature basin        | adc              | thermistor                 |
|             | Temprature laser input  | adc              | thermistor                 |
|             | Temprature laser output | adc              | thermistor                 |

## outputs
| Status      | Name                    | gpio type        | Kind of hardware           |
|-------------|-------------------------|------------------|----------------------------|
|             | Laser enable            | Digital output   | Relay 5v + indicator light |
|             | 230v compressor on      | Digital output   | Relay 5v                   |
|             | Air assist on           | Digital output   | Relay 5v                   |
|             | air suction on          | Digital output   | Relay 5v                   |
|             | Waterpump cooling       | Digital output   | Relay 5v                   |
|             | waterpump tube          | Digital output   | Relay 5v                   |
|             | waterswitch             | Digital output   | Relay 5v                   |
|             | spare                   | Digital output   | Relay 5v                   |

## I2c
| Status      | Name                    | gpio type        | Kind of hardware           |
|-------------|-------------------------|------------------|----------------------------|
| HW done     | lcd screen              | i2c sda          | 20x4 i2c lcd screen        |
| HW done     | lcd screen              | i2c scl          | 20x4 i2c lcd screen        |

## GPIO
| Status      | Name                    | gpio type        | Kind of hardware           |
|-------------|-------------------------|------------------|----------------------------|
| testcondone | sda 20x4 i2c            |                0 |                            |
| testcondone | scl 20x4 i2c            |                1 |                            |
| testcondone | Button encoder          |                2 |                            |
| testcondone | encoder A               |                3 |                            |
| testcondone | Encoder B               |                4 |                            |
|             |                         |                5 |                            |
|             |                         |                6 |                            |
|             |                         |                7 |                            |
|             |                         |                8 |                            |
|             |                         |                9 |                            |
|             |                         |               10 |                            |
|             |                         |               11 |                            |
|             |                         |               12 |                            |
|             |                         |               13 |                            |
|             |                         |               14 |                            |
|             |                         |               15 |                            |
|             |                         |               16 |                            |
|             |                         |               17 |                            |
|             |                         |               18 |                            |
|             |                         |               19 |                            |
|             |                         |               20 |                            |
|             | waterflow sensor        |               21 |                            |
|             |                         |               22 |                            |
|             | temp basin              |               26 |                            |
|             | temp laser out          |               27 |                            |
|             | temp laser in           |               28 |                            |
