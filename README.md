# K40Watchdog
PIco PI W K40 laser watchdog with output &amp; 3 temp sensor 

## table

| sensor inputs           | gpio type        | Kind of hardware                 |
|-------------------------|------------------|----------------------------------|
| Lid front               | switch           | endstop switch                   |
| Lid back                | switch           | endstop switch                   |
| Lid psu                 | switch           | endstop switch                   |
| waterflow in + liters   | digital input    | waterflow sensor                 |
| waterflow out           | switch           | Waterflow on off switch          |
| Temprature basin        | adc              | thermistor                       |
| Temprature laser input  | adc              | thermistor                       |
| Temprature laser output | adc              | thermistor                       |
|                         |                  |                                  |
| user inputs (buttons)   |                  |                                  |
| start cooldown          | switch           |                                  |
| standby for laser       | switch           | enable air assist & sucktion fan |
| Lid override            | switch           | on /off Switch on panel          |
|                         |                  |                                  |
| Outputs                 |                  |                                  |
|                         |                  |                                  |
| Laser enable            | Digital output   | Relay 5v + indicator light       |
| 230v compressor on      | Digital output   | Relay 5v                         |
| Air assist on           | Digital output   | Relay 5v                         |
| air suction on          | Digital output   | Relay 5v                         |
| Waterpump cooling       | Digital output   | Relay 5v                         |
| waterpump tube          | Digital output   | Relay 5v                         |
| waterswitch             | Digital output   | Relay 5v                         |
|                         |                  |                                  |
|                         |                  |                                  |
|                         |                  |                                  |
|                         |                  |                                  |
|                         |                  |                                  |
| screen                  |                  |                                  |
| lcd screen              | i2c sda          |                                  |
| lcd screen              | i2c scl          |                                  |
| rotary encoder knob     | digital input    |                                  |
| rotary encoder knob     | 2x digital input |                                  |
