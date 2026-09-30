from machine import Pin, PWM
from time import sleep

# Motor A / Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Motor B / Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

#LED
led = Pin("LED", Pin.OUT)

# Set PWM frequency to 1000 Hz / Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)

# Estimated power
# 25% = 16383
# 50% = 32767
# 75% = 49181
# 100% = 65535

# Variables
hias = 16383
normi = 32767
seminopee = 49181
nopee = 65535

# Functions
# Move FoCar forward 
# with default values of speed 25% and time 3 seconds
def forward(speed = 16383, time = 3):
    e1.duty_u16(speed)
    e2.duty_u16(speed)
    sleep(time)

# 5 second timeout / 5 sekunnin tauko
sleep(5)

# Move forward / Eteenpäin
m1.value(1)
m2.value(1)

# Move forward for 8 seconds speed 100%
forward(65535, 8)

# Move forward for 10 seconds speed 75%
forward(49181, 10)

# After 10 seconds stop / 10 sekunnin kuluttua pysäytys
sleep(10)
e1.duty_u16(0)
e2.duty_u16(0)

# Wait 1 second for motors to stop / Odota yksi sekunti moottoreiden pysähtymistä
sleep(1)

# Turn left
e2.duty_u16(16383) # left motor 25%
e1.duty_u16(49181) # right motor 75%
