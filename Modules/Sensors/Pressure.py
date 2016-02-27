from numpy.random import random_sample
from datetime import datetime

#Base Sensor Class
from .Sensor import Sensor

class PressureSensor(Sensor):
    """
    A class to handle Pressure sensors
    """

    def __init__(self, ):
        """
        """
        self.sensor_type = 'Pressure'
        self.meas_unit = 'mBar'

    def get_measurement(self):
        #measure value
        if self.computer_connnect:
            value = read_GPIO()

        elif self.RF:
            value = getRFValue()
            
        elif self._debug_mode:
            minTemp = 0
            maxTemp = 1000.0
            value = (maxTemp - minTemp) * random_sample() + minTemp

        time = datetime.now()

        return (time, value)

if __name__ == '__main__':
    p = PressureSensor()
