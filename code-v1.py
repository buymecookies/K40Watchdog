# This script supports the Raspberry Pi Pico board
# Raspberry Pi Pico: http://educ8s.tv/part/RaspberryPiPico
# 20x4 I2C DISPLAY: http://educ8s.tv/part/20x4LCD


import board, busio, time, rotaryio, digitalio, countio

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

# lcd settings
sda, scl = board.GP0, board.GP1
i2c = busio.I2C(scl, sda)
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=4, num_cols=20) #If address 0x27 does not work try 0x3F
lcd.set_cursor_pos(0,1) #because of broken screen

# encoder settings
enc= rotaryio.IncrementalEncoder(board.GP3, board.GP4, 4 )
button = digitalio.DigitalInOut(board.GP2)
button.switch_to_input(pull=digitalio.Pull.DOWN)

# Flowmeter in settings
pin_counter = countio.Counter(board.GP21, edge=countio.Edge.RISE)
flow_frequency = 0


while True:
    if pin_counter.count >= 100:
        pin_counter.reset()
    #print(pin_counter.count * 60 / 7.5)
    flow_rate = (flow_frequency * 60 / 7.5)
    flow_frequency = 0
    time.sleep(0.5)
    


#loop encoder

#while True:
 #   position=enc.position
  #     lcd.print("switch")
   # lcd.print(str(flowin.value))
    #time.sleep(0.36)
    #lcd.clear()
    
    
#lcd.set_cursor_pos(0,1)
#lcd.print("click")

#time.sleep(5)
#lcd.clear()

