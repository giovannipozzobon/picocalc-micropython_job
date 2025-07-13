
import math

from ulab import numpy as np

class Quaternion:

  def __init__(self, real, imag ):
    self._real = real
    self._imag = imag

  def real(self):
    return self._real

  def imag(self):
    return self._imag

  def as_matrix(self):

    w = self._real
    x = self._imag[0]
    y = self._imag[1]
    z = self._imag[2]

    m = np.eye( 4 )
    m[0,0] = 2*(w**2 + x**2)

    m[1,1] = 2*(w**2 + y**2)

    m[2,2] = 2*(w**2 + z**2)

  def __mul__(self, other):
    '''
    '''
    output = Quaternion()
    output.real = self.real * other.real - self.imag  * other.imag
    output.imag = self.real * other.imag + other.real * self.imag + np.cross( self.imag, other.imag )

    return output

  @staticmethod
  def from_angle_axis( theta, vec, degrees = False ):

    # Convert arrays to np
    if isinstance(vec,list):
      vec = np.array( vec )

    #  check if degrees requested
    if degrees:
      theta = math.degrees( theta )

    real = np.dot( math.cos( theta / 2 ), vec )
    imag = np.dot( math.sin( theta / 2 ), vec )

    return Quaternion( real, imag )

