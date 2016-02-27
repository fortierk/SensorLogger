from numpy.random import random_sample
from datetime import datetime

#Base Sensor Class
from Sensor import Sensor

class MoistureSensor(Sensor):
    """
    A class to Moisture sensors
    """

    def __init__(self, ):
        """
        """
        self.sensor_type = 'Moisture'
        self.meas_unit = '% Water'

    def get_measurement(self):
        #measure value
        if self.computer_connnect:
            value = read_GPIO()

        elif self.RF:
            value = get_RF_Value()
        elif self._debug_mode:
            value = random_sample()
            
        time = datetime.now()

        return (time, value)

if __name__ == '__main__':
    m = MoistureSensor()
