from enum import IntEnum

# I2C device addresses

LSM303D_Address = 0x1D  # Accelerometer & Magnetometer
L3GD20H_Address = 0x6B  # Gyroscope


class LSM303D(IntEnum):
    STATUS_M = 0x07
    OUT_X_L_M = 0x08
    OUT_X_H_M = 0x09
    OUT_Y_L_M = 0x0A
    OUT_Y_H_M = 0X0B
    OUT_Z_L_M = 0x0C
    OUT_Z_H_M = 0x0D
    WHO_AM_I = 0x0
    CTRL0 = 0x1F
    CTRL1 = 0x20
    CTRL2 = 0x21
    CTRL3 = 0x22
    CTRL4 = 0x23
    CTRL5 = 0x24
    CTRL6 = 0x25
    CTRL7 = 0x26
    STATUS_A = 0x2
    OUT_X_L_A = 0x28
    OUT_X_H_A = 0x29
    OUT_Y_L_A = 0x2A
    OUT_Y_H_A = 0x2B
    OUT_Z_L_A = 0x2C
    OUT_Z_H_A = 0x2D