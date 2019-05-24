from AltIMU_v3 import AltIMUv3
from RPi import GPIO
import time
import Activity_3 as Integral

# Global variable declaration
LED1 = 17
LED2 = 21
LED3 = 22
LED4 = 10
Button = 18
count = 0
sampling_period, value = 0.1, 0
accel = [0, 0, 0]
area = [0, 0, 0]
bias = [0, 0, 0]

# GPIO Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LED1, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)
GPIO.setup(Button, GPIO.IN)
GPIO.output(LED1,False)
GPIO.output(LED2,False)
GPIO.output(LED3,False)
GPIO.output(LED4,False)


# AltIMU setup
altimu = AltIMUv3()
altimu.enable_accelerometer()
altimu.enable_gyroscope()

def calibrate():
    # Calibration process with 1000 samples, returning the bias and
    # last values measured
    print('Calibrating...')
    sum_gyro = [0, 0, 0]

    for i in range(0, 1000):
        gyro = altimu.get_gyroscope_cal()

        for x in range(0, 3):
            sum_gyro[x] += gyro[x]

    for j in range(0, 3):
        bias[j] = sum_gyro[j]/1000
    print('Done calibrating.')

    return bias, gyro

def sample(bias, previous):
    # Sample acquisition
    real_gyro = [0, 0, 0]
    gyro = altimu.get_gyroscope_cal()
    accel = altimu.get_accelerometer_cal()

    # Area calculation
    for x in range(0, 3):
        real_gyro[x] = gyro[x] - bias[x]
        area[x] += ((real_gyro[x] + previous[x])/2)*sampling_period
    time.sleep(sampling_period)

    return area, real_gyro, accel


# Button loop
while value == 0:
    value = GPIO.input(Button)
bias, previous = calibrate()
reset = time.time()

while True:
    # Sample evaluation and LED activations
    angle, new_previous, accel = sample(bias, previous)
    previous = new_previous
    new_accel = altimu.get_accelerometer_cal()
    diff = new_accel[0] - accel[0]

    if angle[2] >= 90 and count == 0:
        GPIO.output(LED1,True)
        count += 1
        reset = time.time()
    if diff > 0.3 and count == 1:
        GPIO.output(LED2,True)
        count += 1
        reset = time.time()
    if angle[0] <= -90 and count == 2:
        GPIO.output(LED3,True)
        accel_new = accel[0]
        count += 1
        reset = time.time()
    if accel[2] <= -1 and count == 3:
        GPIO.output(LED4,True)
        count += 1
        reset = time.time()

    if (time.time() - reset) > 5:
        count = 0
        angle = [0, 0, 0]
        GPIO.output(LED1,False)
        GPIO.output(LED2,False)
        GPIO.output(LED3,False)
        GPIO.output(LED4,False)
        reset = time.time()
