from AltIMU_v3 import AltIMUv3
from RPi import GPIO
import time
from ADC import MCP3204

'''
This program performs as the main class of all the Bicep analizer.

MCP3204(): This is the class of the Analog to Digital Converter, which measures
the quantity of voltage respecting with the Vref, which is 3.3V. The given
value will be expressed in bits in the range of 0-4096, as 0V-3.3V, giving steps
of approximately 0.8mV per bit.

AltIMUv3(): This class controls the AltiMU via I2C, which contains the
gyroscope sensor, that will be an important element in the detection of
the exercise correct performing.
'''
adc = MCP3204()
altimu = AltIMUv3()
altimu.enable_gyroscope()
initial_zero, previous = 0, 0
area, actual, sampling_period, value = 0, 0, 0.001, 0


errors = []


start_time = time.time()



def calibrate(rate):
    '''
This method performs an average of "rate" values to bring a bias that will
aid to get the point of reference of the gyroscope.

rate(int): This value determines the number values obtained from the gyroscope
to perform the average.
    '''
    print("Calibrating..")
    average = 0
    
    for i in range(0, rate):
        gyro = altimu.get_gyroscope_cal()
        average += gyro[2]
        
    average = average/rate
    last_sample = gyro[2]
    print("Done calibrating")
    
    return average, last_sample



bias, previous = calibrate(1000)
right_reps = 0
left_reps = 0
fast_reps = 0
total_reps = 0
print("Start workout")

try:
    
    while True:
        '''
This loop obtains the actual angular position respecting with the
initial(biased) value. This will aid to determine the perform of the
routine.
        '''


        gyro = altimu.get_gyroscope_cal()
        actual = gyro[2] - bias
        area += ((actual + previous)/2)*sampling_period
        previous = actual
        time.sleep(sampling_period)
        Input = adc.read(adc_channel=0)
##        print(Input)
        if total_reps < 4:
            
            if Input > 1900:
                total_reps += 1
                print(total_reps, "reps done")
                
                if area > 10:
                    right_reps += 1
                    
                elif area < -10:
                    left_reps += 1
                    
                if actual > 40:
                    fast_reps += 1
                    
                time.sleep(3)
             
        else:
            wrong_reps = right_reps + left_reps + fast_reps
            accuracy = str(int(((total_reps-wrong_reps)/total_reps)*100))
            print("Finished workout")
            print("Total reps: ", total_reps)
            print("Wrong reps: ", wrong_reps)
            print("Accuracy: ", accuracy, "% \n \n")

            if right_reps > 0:
                print(right_reps, "repetitions were too far to the right")
            if left_reps > 0:
                print(left_reps, " repetitions were too far to the left")
            if fast_reps > 0:
                print(fast_reps, " repetitions were too fast")
            
            break 

    
except:
    print('What is going on?')


        






    
    


        
