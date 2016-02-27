from numpy.random import random_sample
from datetime import datetime

#Base Sensor Class
from .Sensor import Sensor

class TemperatureSensor(Sensor):
    """
    A class to handle temperature sensors
    """

    def __init__(self, ):
        """
        """
        self.sensor_type = 'Temperature'
        self.meas_unit = 'F'

    def get_measurement(self):
        #measure value
        if self.computer_connnect:
            value = read_GPIO()

        elif self.RF:
            value = getRFValue()
        elif self._debug_mode:
            minTemp = -20.0
            maxTemp = 100.0
            value = (maxTemp - minTemp) * random_sample() + minTemp

        time = datetime.now()

        return (time, value)


if __name__ == '__main__':
    t = TemperatureSensor()
    t.chip_ID = 'TMP36GT9Z-ND'   