#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#
#*                                                                                    *#
#*                           Copyright (c) 2025 Terminus LLC                          *#
#*                                                                                    *#
#*                                All Rights Reserved.                                *#
#*                                                                                    *#
#*          Use of this source code is governed by LICENSE in the repo root.          *#
#*                                                                                    *#
#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#

#  Python Libraries
from time import *

#  Ulab
import ulab as np


#  Enumerations
TYPE_ECEF = 0
TYPE_GEO  = 1
TYPE_UTM  = 2

class Base:
    '''
    Base Coordinate Type
    '''

    def __init__(self):
        pass

class ECEF(Base):

    def __init__( self, data ):
        self.data = data

    @staticmethod
    def from_xyz( x, y, z ):
        return ECEF( np.array( [ x, y, z ] ) )


class Geographic(Base):
    '''
    Geographic Coordinate System
    '''

    def __init__( self,
                  lat_deg: float,
                  lon_deg: float,
                  elev_m:  float ):

        self.lat_deg = lat_deg
        self.lon_deg = lon_deg
        self.elev_m  = elev_m

        super().__init__()

    def latitude( self, degrees: bool = True ):
        if degrees:
            return self.lat_deg
        else:
            return math.radians(self.lat_deg)

    def longitude( self, degrees: bool = True ):
        if degrees:
            return self.lon_deg
        else:
            return math.radians(self.lon_deg)

    def elevation(self):
        return self.elev_m

    @staticmethod
    def from_lla( lat_deg: float,
                  lon_deg: float,
                  elev_m:  float = 0 ):

        return Geographic( lat_deg = lat_deg,
                           lon_deg = lon_deg,
                           elev_m  = elev_m )


class UTM(Base):

    def __init__( self ):
        self.grid_zone  = 0
        self.hemisphere = True
        self.easting    = 0
        self.northing   = 0
        self.elev_m     = 0

class Factory:

    @staticmethod
    def create( tp ):
        if tp == TYPE_ECEF:
            return ECEF()
        if tp == TYPE_UTM:
            return UTM()
        return Geo()



