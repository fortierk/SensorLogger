# import RPi.GPIO as GPIO

class Sensor(object):
    """
    A Base class to handle sensors
    """

    def __init__(self,
                 sensor_type='',
                 chip_ID='',
                 location='Living_room',
                 GPS_location=None,
                 GPS_chip_ID='',
                 outside=False,
                 meas_unit='',
                 RF=False,
                 RF_chip_ID=''):
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

    def __repr__(self):
        return (('Sensor(sensor_type=%s,chip_ID=%s,location=%s, GPS_location=%s, GPS_chip_ID=%s, outside=%s,' +
                 'meas_unit=%s, RF=%s, computer_connected=%s, _debug_mode=%s)')
                %
                (repr(self.sensor_type), repr(self.chip_ID), repr(self.location), repr(self.GPS_location),
                 repr(self.GPS_chip_ID), repr(self.outside), repr(self.meas_unit), repr(self.RF),
                 repr(self.computer_connnect), repr(self._debug_mode))
                )

if __name__ == '__main__':
    s = Sensor()
