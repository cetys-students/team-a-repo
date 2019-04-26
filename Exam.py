from AltIMU_v3 import AltIMUv3
import Activity_3 as integral
import RPi.GPIO as GPIO
import time

# Setup
LED = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
altimu = AltIMUv3()
altimu.enable_gyroscope()
altimu.enable_accelerometer()
GPIO.output(LED,GPIO.LOW)

while True:
    # Data readings
    accel= altimu.get_accelerometer_cal() 
    gyro = altimu.get_gyroscope_cal()
    accel_z = accel[2]
    gyro_x = gyro[0]
    gyro_y = gyro[1]

    #Data evalutation
    if accel_z < 0.6 and gyro_x > 250 or gyro_y < -200 : 
        GPIO.output(LED,GPIO.HIGH)
        time.sleep(0.3)
    GPIO.output(LED,GPIO.LOW)


    
                
                    

