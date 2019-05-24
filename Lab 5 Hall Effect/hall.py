import I2C_LCD_driver
import time
import RPi.GPIO as GPIO
import math ##math.pi
import datetime

#Variables
mylcd = I2C_LCD_driver.lcd()
pinSpeed1 = 18
pinSpeed2 = 23
pinSpeed3 = 24
pinMeasure1 = 5
pinMeasure2 = 6
pinMeasure3 = 13
pinMeasure4 = 19
pinHall = 17
motorPWM = 27
DC = 0
Hertz = 0
RPM = 0
angularVelocity = 0
degreesPerSecond = 0

#Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinSpeed1, GPIO.IN)
GPIO.setup(pinSpeed2, GPIO.IN)
GPIO.setup(pinSpeed3, GPIO.IN)
GPIO.setup(pinMeasure1, GPIO.IN)
GPIO.setup(pinMeasure2, GPIO.IN)
GPIO.setup(pinMeasure3, GPIO.IN)
GPIO.setup(pinMeasure4, GPIO.IN)
GPIO.setup(pinHall, GPIO.IN)
GPIO.setup(motorPWM, GPIO.OUT)
pwm = GPIO.PWM(motorPWM, 100)
pwm.start(DC)
mylcd.lcd_clear()

while True:
#PWM Duty Cycle setup
    if GPIO.input(pinSpeed1) == 1:
        DC = 30
        pwm.start(DC)
    if GPIO.input(pinSpeed2) == 1:
        DC = 55
        pwm.start(DC)
    if GPIO.input(pinSpeed3) == 1:
        DC = 68
        pwm.start(DC)
#Measure repetitions per second
    timeEnd = time.time() + 2
    while time.time() < timeEnd:
        if GPIO.input(pinHall) == 1:
            Hertz += 1
            time.sleep(0.06)
    Hertz = Hertz/2
#Display in desired units
    mylcd.lcd_clear()
    if GPIO.input(pinMeasure1) == 1: #RAD/s
        angularVelocity = 2*math.pi*Hertz
        mylcd.lcd_display_string(str(angularVelocity), 1)
        mylcd.lcd_display_string("RAD/s", 2)
    if GPIO.input(pinMeasure2) == 1: #DEG/s
        degreesPerSecond = 360*Hertz
        mylcd.lcd_display_string(str(degreesPerSecond), 1)
        mylcd.lcd_display_string("DEG/s", 2)
    if GPIO.input(pinMeasure3) == 1: #Hertz
        mylcd.lcd_display_string(str(Hertz), 1)
        mylcd.lcd_display_string("Hertz", 2)
    if GPIO.input(pinMeasure4) == 1: #RPM
        RPM = 60*Hertz
        mylcd.lcd_display_string(str(RPM), 1)
        mylcd.lcd_display_string("RPM", 2)
    Hertz = 0
    RPM = 0
    angularVelocity = 0
    degreesPerSecond = 0      



