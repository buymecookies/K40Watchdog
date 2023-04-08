# K40Watchdog
PIco PI W K40 laser watchdog with output &amp; 3 temp sensor 

## table

| Status  | sensor inputs           | gpio type        | Kind of hardware                 |
|---------|-------------------------|------------------|----------------------------------|
|         | Lid front               | switch           | endstop switch                   |
|         | Lid back                | switch           | endstop switch                   |
|         | Lid psu                 | switch           | endstop switch                   |
| HW done | waterflow in + liters   | digital input    | waterflow sensor                 |
|         | waterflow out           | switch           | Waterflow on off switch          |
|         | Temprature basin        | adc              | thermistor                       |
|         | Temprature laser input  | adc              | thermistor                       |
|         | Temprature laser output | adc              | thermistor                       |
|         |                         |                  |                                  |

| Status  | user inputs (buttons)   | gpio type        | Kind of hardware                 |
|---------|-------------------------|------------------|----------------------------------|
|         | start cooldown          | switch           |                                  |
|         | standby for laser       | switch           | enable air assist & sucktion fan |
|         | Lid override            | switch           | on /off Switch on panel          |
|         |                         |                  |                                  |

| Status  | Outputs                 | gpio type        | Kind of hardware                 |
|---------|-------------------------|------------------|----------------------------------|
|         | Laser enable            | Digital output   | Relay 5v + indicator light       |
|         | 230v compressor on      | Digital output   | Relay 5v                         |
|         | Air assist on           | Digital output   | Relay 5v                         |
|         | air suction on          | Digital output   | Relay 5v                         |
|         | Waterpump cooling       | Digital output   | Relay 5v                         |
|         | waterpump tube          | Digital output   | Relay 5v                         |
|         | waterswitch             | Digital output   | Relay 5v                         |
|         |                         |                  |                                  |
| Status  | screen                  | gpio type        | Kind of hardware                 |
| HW done | lcd screen              | i2c sda          |                                  |
| HW done | lcd screen              | i2c scl          |                                  |
| HW done | rotary encoder switch   | digital input    |                                  |
| HW done | rotary encoder knob     | 2x digital input |                                  |
|         |                         |                  |                                  |

| Status  | Type                    | gpio             | Kind of hardware                 |
|---------|-------------------------|------------------|----------------------------------|
|         | sda 20x4 i2c            |                0 |                                  |
|         | scl 20x4 i2c            |                1 |                                  |
|         | Button encoder          |                2 |                                  |
|         | encoder A               |                3 |                                  |
|         | Encoder B               |                4 |                                  |
|         |                         |                5 |                                  |
|         |                         |                6 |                                  |
|         |                         |                7 |                                  |
|         |                         |                8 |                                  |
|         |                         |                9 |                                  |
|         |                         |               10 |                                  |
|         |                         |               11 |                                  |
|         |                         |               12 |                                  |
|         |                         |               13 |                                  |
|         |                         |               14 |                                  |
|         |                         |               15 |                                  |
|         |                         |               16 |                                  |
|         |                         |               17 |                                  |
|         |                         |               18 |                                  |
|         |                         |               19 |                                  |
|         |                         |               20 |                                  |
|         | waterflow sensor        |               21 |                                  |
|         |                         |               22 |                                  |
|         | temp basin              |               26 |                                  |
|         | temp laser out          |               27 |                                  |
|         | temp laser in           |               28 |                                  |
