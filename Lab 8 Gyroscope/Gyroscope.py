from AltIMU_v3 import AltIMUv3
from RPLCD import CharLCD
from RPi import GPIO
import time
import Activity_3 as Integral

# LCD and GPIO Setup
LCD = CharLCD(cols = 16, rows = 2, pin_rs = 37, pin_e = 35, pins_data = [33,31,29,23])
Button = 12
GPIO.setup(Button, GPIO.IN)
altimu = AltIMUv3()
altimu.enable_gyroscope()
LCD.clear()
initial_zero, previous = 0, 0
LCD.write_string(u'Press the button to start...')
area, actual, sampling_period, value = 0, 0, 0.1, 0

# Calibration function
def calibrate():
    average = 0
    LCD.clear()
    LCD.write_string(u'Calibrating...')
    for i in range(0, 1000):
        gyro = altimu.get_gyroscope_cal()
        average += gyro[2]
    average = average/1000
    last_sample = gyro[2]
    return average, last_sample

# Button while loop
while value == 0:
    value = GPIO.input(Button)

# First calibration
bias, previous = calibrate()

# Data aquisition and processing
while True:
    gyro = altimu.get_gyroscope_cal()
    actual = gyro[2] - bias
    area += ((actual + previous)/2)*sampling_period
    previous = actual
    LCD.write_string(str(area))
    value = GPIO.input(Button)
    if value == 1:
        area = 0
        bias, previous = calibrate()
    time.sleep(sampling_period)
    LCD.clear()
