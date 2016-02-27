# -------------------------------------------------------------------------------
# Name:        Temperature.py
# Purpose:     Python class to log data from a temperature sensor.
# Author:      Kevin Fortier <fortierk@gmail.com>
# Licence:     MIT License
#              This file is subject to the terms and conditions of the MIT License.
#              For further details, please refer to LICENSE.txt
# Revision:    0.0.1
# -------------------------------------------------------------------------------
from datetime import datetime
from numpy.random import random_sample

#Base Sensor Class
from Sensor import Sensor

class TemperatureSensor(Sensor):
    """
    A class to handle temperature sensors
    """

    def __init__(self,
                 meas_unit='F',
                 DAC_name=''):
        """
        """
        super(TemperatureSensor, self).__init__(meas_unit=meas_unit)
        self.sensor_type = 'Temperature'
        self.DAC_name = 'TMP36GT9Z-ND'
    def get_measurement(self):
        #measure value
        if self.computer_connnect:
            value = self.read_GPIO()

        elif self.RF:
            value = self.getRFValue()
        elif self._debug_mode:
            minTemp = -20.0
            maxTemp = 100.0
            value = (maxTemp - minTemp) * random_sample() + minTemp
        else:
            value = -1.0

        time = datetime.now()

        return time, value


if __name__ == '__main__':
    t = TemperatureSensor()
    t.chip_ID = 'TMP36GT9Z-ND'
    print t
