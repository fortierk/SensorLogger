# -------------------------------------------------------------------------------
# Name:        Pressure.py
# Purpose:     Python class to log data from a pressure sensor.
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

class PressureSensor(Sensor):
    """
    A class to handle Pressure sensors
    """

    def __init__(self):
        """
        """
        super(PressureSensor, self).__init__()
        self.sensor_type = 'Pressure'
        self.meas_unit = 'mBar'

    def get_measurement(self):
        #measure value
        if self.computer_connnect:
            value = self.read_GPIO()

        elif self.RF:
            value = self.get_RF_Value()
            
        elif self._debug_mode:
            minTemp = 0
            maxTemp = 1000.0
            value = (maxTemp - minTemp) * random_sample() + minTemp
        else:
            value = -1.0

        time = datetime.now()

        return (time, value)

if __name__ == '__main__':
    p = PressureSensor()
    print p
