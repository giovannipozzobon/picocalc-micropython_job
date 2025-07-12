
import math

import ndarray as np

def to_rotmat( theta, axis, fmt = 'rad', dims = (4,4) ):
   
   if fmt == 'deg':
     theta = math.radians( theta )
   
   mat = np.eye( dims = dims )
   axis = str(axis).lower()
   if axis == 'x':
     mat[1,1] = math.cos(theta)
     mat[1,2] = -math.sin(theta)
     mat[2,1] = math.sin(theta)
     mat[2,2] = math.cos(theta)
     
   elif axis == 'y':
     mat[0,0] = math.cos(theta)
     mat[0,2] = math.sin(theta)
     mat[2,0] = -math.sin(theta)
     mat[2,2] = math.cos(theta)
     
   elif axis == 'z':
     mat[0,0] = math.cos(theta)
     mat[0,1] = math.sin(theta)
     mat[1,0] = -math.sin(theta)
     mat[1,1] = math.cos(theta)
     
   else:
     raise Exception('Unsupported Axis: {}'.format(axis))
   
   return mat
     
