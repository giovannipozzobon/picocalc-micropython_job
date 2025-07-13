#    File:    ovt_plat_to_target.py
#    Author:  Marvin Smith
#    Date:    7/8/2025
#
#    Purpose:  Convert Platform coordinates to Az/El Angles
#

#--------------------------------------#
#-         Script Dependencies        -#
#--------------------------------------#

#  Micropython Libraries
import logging
import math

from ulab import numpy as np

# Geo-Tools Libraries
import geotools
from geotools.coordinate import Geographic
from geotools.ovt_math   import platform_to_ned

#------------------------------------#
#-       User Input Area            -#
#------------------------------------#

#  Sensor Position
pos_geo = Geographic.from_lla( lat_deg = 39.5445046,
                               lon_deg = -104.8450277,
                               elev_m  = 1788.816 )

#  Sensor Angles
yaw_deg   = 176.750286
pitch_deg = -4.029380
roll_deg  = 177.101864

#  Platform Vector
platform_vec = np.array( [[0],[0],[-1]] )

#------------------------------------#
#-          Program Logic           -#
#------------------------------------#
def launch():

  # Convert angles to radians
  yaw_rad   = math.radians( yaw_deg )
  pitch_rad = math.radians( pitch_deg )
  roll_rad  = math.radians( roll_deg )

  #  Convert to NED
  ned_vec = platform_to_ned( platform_vec,
                             yaw_rad,
                             pitch_rad,
                             roll_rad )

  logging.info( f'NED Vector: {ned_vec}' )


if __name__ == '__main__':
    try:
        logging.basicConfig( level = logging.INFO )

        logging.debug( 'Start of application' )
        launch()
    except Exception as e:
        print( f'error occurred: {e}' )
