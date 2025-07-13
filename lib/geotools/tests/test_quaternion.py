
from ulab import numpy as np

#  Project Libraries
from geotools.quaternion import Quaternion


def test_Quaternion_angle_axis():

    v1 = np.array( [[1],[0],[0]] )
    q1 = Quaternion.from_angle_axis( 45, v1, degrees=True )


test_Quaternion_angle_axis()