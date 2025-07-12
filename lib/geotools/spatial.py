
#  Micropython Libraries
import math

#  Numerical Python
from ulab import numpy as np

def rotation_matrix( axes   : str,
                     angles : list,
                     degrees: bool = False,
                     dims   : tuple = (4,4) ):
    """
    Construct a rotation matrix
    """
    
    if len(axes) != len(angles):
        raise Exception( f'Length of axis list and angle list must be equal. {len(axes)} vs {len(angles)}' )
    
    mat = None
    for x in range( len( axes ) ):

        # Index
        axis  = str(axes[x]).lower()
        angle = angles[x]

        if degrees:
            angle = math.radians( angle )

        tmp = np.eye( dims, dtype = float )

        if axis == 'x':

            tmp[1,1] =  math.cos( angle )
            tmp[1,2] = -math.sin( angle )
            tmp[2,1] =  math.sin( angle )
            tmp[2,2] =  math.cos( angle )

        elif axis == 'y':

            tmp[0,0] =  math.cos( angle )
            tmp[0,2] =  math.sin( angle )
            tmp[2,0] = -math.sin( angle )
            tmp[2,2] =  math.cos( angle )

        elif axis == 'z':

            tmp[0,0] =  math.cos( angle )
            tmp[0,1] = -math.sin( angle )
            tmp[1,0] =  math.sin( angle )
            tmp[1,1] =  math.cos( angle )

        else:
            raise Exception( 'Unsupported axis: {}'.format( axis ) )


        if mat is None:
            mat = tmp
        else:
            mat = mat * tmp

    return mat

def enu_to_ned_matrix( dims: tuple = (4,4) ):

    mat = np.zeros( dims )

    mat[0,1] =  1
    mat[1,0] =  1
    mat[2,2] = -1
    mat[3,3] =  1

    return mat


