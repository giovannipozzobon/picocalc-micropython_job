
#  Micropython Libraries
import math

#  Numerical Python
from ulab import numpy as np

#  Geotools Libraries
from geotools.spatial import enu_to_ned_matrix, rotation_matrix

#  Platform to NED
def platform_to_ned( platform_vec : np.array,
                     yaw_rad      : float,
                     pitch_rad    : float,
                     roll_rad     : float ):

    #  ENU to NED transform
    M_enu2ned = enu_to_ned_matrix()

    #  Pitch Adj
    M_pitch = rotation_matrix( 'y', [ math.pi/2.0 ] )
    M_roll  = rotation_matrix( 'x', [ math.pi] )

    M_plat2ned = M_roll * M_pitch * M_enu2ned

    return M_plat2ned * platform_vec

