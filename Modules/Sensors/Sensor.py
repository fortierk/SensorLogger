import RPi.GPIO as GPIO

class Sensor(object):
    """
    A Base class to handle sensors
    """
    def __init__(self, sensor_type='', chip_ID='', location='Living_room',
                 GPS_location = None, GPS_chip_ID='', outside=False,
                 meas_unit ='', RF=False, RF_chip_ID=''):
        """
        """
        self.sensor_type = sensor_type
        self.chip_ID = chip_ID
        self.location = location
        self.GPS_location = GPS_location
        self.GPS_chip_ID = GPS_chip_ID
        self.outside = outside
        self.meas_unit = meas_unit
        self.RF = RF
        self.computer_connnect = True
        self._debug_mode = True


    def read_GPIO(self):
        pass

    def read_RF_value(self):
        pass

    


if __name__ == '__main__':
    s = Sensor()