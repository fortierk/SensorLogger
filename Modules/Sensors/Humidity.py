from numpy.random import random_sample
from datetime import datetime


#Base Sensor Class
from .Sensor import Sensor

class HumiditySensor(Sensor):
    """
    A class to handle Pressure sensors
    """

    def __init__(self, ):
        """
        """
        self.sensor_type = 'Hummidity'
        self.meas_unit = '% Water'

    def get_measurement(self):
        #measure value
        if self.computer_connnect:
            value = read_GPIO()

        elif self.RF:
            value = getRFValue()
            
        elif self._debug_mode:
            minTemp = 0
            maxTemp = 100.0
            value = (maxTemp - minTemp) * random_sample() + minTemp

        time = datetime.now()

        return (time, value)

if __name__ == '__main__':
    h = PressureSensor()
