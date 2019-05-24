from AltIMU_v3 import AltIMUv3
from RPLCD import CharLCD
from RPi import GPIO
import time
import math
import Activity_3 as Integral

# Setup
LED1 = 17
LED2 = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
altimu = AltIMUv3()
altimu.enable_accelerometer()
accel = altimu.get_accelerometer_cal()
lowest_value = 0.90
highest_value = 1.1
Limit1 = -0.85
Limit2 = -1.15
while True:
    accel = altimu.get_accelerometer_cal()
    accel_z = accel[2]
    gravity = math.sqrt(math.pow(accel[0],2)+math.pow(accel[1],2)+math.pow(accel[2],2))
    if lowest_value <= gravity <= highest_value:
        GPIO.output(LED1,True)
        print('stable')
        if Limit2 <= accel_z <= Limit1:
            GPIO.output(LED2,True)
        
    else:
        GPIO.output(LED1,False)
        GPIO.output(LED2,False)
        print('movement')

    
