# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        DatabaseLogger.py
# Purpose:     Python database class for interfacing with SQL database to hold 
#              measurements.
# Author:      Kevin Fortier <fortierk@gmail.com>
# Licence:     MIT License
#              This file is subject to the terms and conditions of the MIT License.
#              For further details, please refer to LICENSE.txt
# Revision:    0.0.1
# -------------------------------------------------------------------------------
class DatabaseLogger(object):
    """
    """
    
    def __init__(self, ):
        """
        """
        self.filename = 'test.sql'

    def get_measurements(self):
        pass

    def create_database(self,filename):
        pass

    def log_measurement(self,filename):
        pass
        
if __name__ == '__main__':
    d = DatabaseLogger()
