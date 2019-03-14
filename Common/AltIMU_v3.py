from I2C import I2C
from constants import *


class AltIMUv3(I2C):

    # Output registers used by the accelerometer
    accel_registers = [
        LSM303D.OUT_X_L_A,
        LSM303D.OUT_X_H_A,
        LSM303D.OUT_Y_L_A,
        LSM303D.OUT_Y_H_A,
        LSM303D.OUT_Z_L_A,
        LSM303D.OUT_Z_H_A,
    ]

    def __init__(self, bus_id=1):
        """ 
        Set up I2C connection and initialize some flags and values.
        """

        super(AltIMUv3, self).__init__(bus_id)
        self.is_accel_enabled = False

    def __del__(self):
        """ 
        Clean up.
        """
        try:
            # Power down MEMS
            self.write_register(LSM303D_Address, LSM303D.CTRL1, 0x00)

            super(AltIMUv3, self).__del__()
        except:
            pass

    def enable(self, accelerometer=True):
        if accelerometer:
            self.write_register(LSM303D_Address, LSM303D.CTRL1, 0xA7)
            self.write_register(LSM303D_Address, LSM303D.CTRL2, 0x00)
            self.is_accel_enabled = True

    def get_accelerometer_raw(self):
        """
        Return a 3D vector of raw accelerometer data.
        """

        # Check if accelerometer has been enabled
        if not self.is_accel_enabled:
            raise(Exception('Accelerometer is not enabled!'))

        return self.read_sensor(LSM303D_Address, self.accel_registers)

    def get_accelerometer_cal(self):
        """
        Return a 3D vector of calibrated accelerometer data.
        """
        raw = self.get_accelerometer_raw()
        scaling = 0.061 / 1000

        cal_x = raw[0] * scaling
        cal_y = raw[1] * scaling
        cal_z = raw[2] * scaling

        return [cal_x, cal_y, cal_z]