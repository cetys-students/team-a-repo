from math import *


def float_range(x, y, jump):
    # Samples for a sine signal
    samples = []
    while x < y:
        samples.append(sin(x))
        x += jump
    return samples


def definite_integral(samples, lower_limit, upper_limit, sampling_period):

    # Check if the limits are valid
    if lower_limit >= upper_limit:
        return 0.0

    # Do the integral
    sum = 0.5 * (samples[lower_limit] + samples[upper_limit])
    for i in range(lower_limit, len(samples)):
        sum += samples[i]
    result = sampling_period * sum
    return result


def sample_integral(samples, sampling_period):

    # Initialization of variables and area calculation
    area = 0
    result = []
    for i in range(0, len(samples)-1):
        area += ((samples[i] + samples[i+1])*sampling_period)/2
        result.append(area)
    return result
    
