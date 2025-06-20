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

#  TI/PicoCalc Libraries
import turtle

from ui import Button, Check_Box, HBoxLayout, Header, Label, Page, Text_Input, VBoxLayout

#  Enumerations
TYPE_ECEF    = 0
TYPE_GEO_DD  = 1
TYPE_GEO_DM  = 2
TYPE_GEO_DMS = 3
TYPE_UTM     = 4

INPUT_WOUNDS = { TYPE_ECEF:    3,
                 TYPE_GEO_DD:  3,
                 TYPE_GEO_DM:  6,
                 TYPE_GEO_DMS: 8 }

#------------------------------------#
#-      Convert Type to String      -#
#------------------------------------#
def type_to_string( tp ):
    if tp == TYPE_ECEF:
        return 'Earth-Centered, Earth-Fixed'
    if tp == TYPE_GEO_DD:
        return 'Geographic, Decimal-Degrees'
    if tp == TYPE_GEO_DM:
        return 'Geographic, Degree-Minutes'
    if tp == TYPE_GEO_DMS:
        return 'Geographic, Degree-Minute-Seconds'
    if tp == TYPE_UTM:
        return 'Universal Transverse Mercator'
    
    raise Exception('Unsupported')


class Base:
    '''
    Base Coordinate Type
    '''
  
    def __init__(self):
        pass

class ECEF(Base):

    def __init__( self ):
        self.x = ''
        self.y = ''
        self.z = ''


class Geo(Base):
    '''
    Geographic Coordinate System
    '''
  
    def __init__( self ):
        self.lat_deg = ''
        self.lon_deg = ''
        self.elev_m  = ''

        super().__init__(self)


class UTM(Base):

    def __init__( self ):
        self.grid_zone  = ''
        self.hemisphere = ''
        self.easting    = ''
        self.northing   = ''
        self.elev_m     = ''

class Factory:

    @staticmethod
    def create( tp ):
        if tp == TYPE_ECEF:
            return ECEF()
        if tp == TYPE_UTM:
            return UTM()
        return Geo()

#---------------------------------#
#-       Geographic Input        -#
#---------------------------------#
def geo_dd_input( is_input ):

    layout = VBoxLayout()

    layout.add_widget( Label( title = 'Geo Decimal Degrees' ) )

    #  Span layout
    temp_layout = HBoxLayout()
    layout.add_widget( temp_layout )

    #  Column 1:  Lat/Lon
    c1_layout = VBoxLayout()
    temp_layout.add_widget( c1_layout )
    c1_layout.add_widget( Text_Input( label_text = 'Latitude: ' ) )
    c1_layout.add_widget( Text_Input( label_text = 'Longitude: ' ) )
    
    #  Column 2:  Format
    c2_layout = VBoxLayout()
    temp_layout.add_widget( c2_layout )

    c2_layout.add_widget( Check_Box( label_text = 'deg', is_active = True ) )
    c2_layout.add_widget( Check_Box( label_text = 'rad', is_active = False ) )

    return layout

def geo_dm_input( is_input ):
    
    layout = VBoxLayout()

    layout.add_widget( Label( title = 'Geo Degree-Minutes' ) )

    #  Latitude Inputs
    layout.add_widget( Label( title = 'Latitude' ) )
    lat_layout = HBoxLayout()
    layout.add_widget( lat_layout )

    lat_layout.add_widget( Text_Input( label_text = 'Deg: ' ) )
    lat_layout.add_widget( Text_Input( label_text = 'Min: ' ) )


    #  Longitude Inputs
    layout.add_widget( Label( title = 'Longitude' ) )
    lon_layout = HBoxLayout()
    layout.add_widget( lon_layout )

    lon_layout.add_widget( Text_Input( label_text = 'Deg: ' ) )
    lon_layout.add_widget( Text_Input( label_text = 'Min: ' ) )

    return layout

def geo_dms_input( is_input ):
    
    layout = VBoxLayout()

    layout.add_widget( Label( title = 'Geo Degree-Minutes-Seconds' ) )

    #  Latitude Inputs
    layout.add_widget( Label( title = 'Latitude' ) )
    lat_layout = HBoxLayout()
    layout.add_widget( lat_layout )

    lat_layout.add_widget( Text_Input( label_text = 'Deg: ', input_width = 50 ) )
    lat_layout.add_widget( Text_Input( label_text = 'Min: ', input_width = 50 ) )
    lat_layout.add_widget( Text_Input( label_text = 'Secs: ', input_width = 75 ) )


    #  Longitude Inputs
    layout.add_widget( Label( title = 'Longitude' ) )
    lon_layout = HBoxLayout()
    layout.add_widget( lon_layout )

    lon_layout.add_widget( Text_Input( label_text = 'Deg: ', input_width = 50 ) )
    lon_layout.add_widget( Text_Input( label_text = 'Min: ', input_width = 50 ) )
    lon_layout.add_widget( Text_Input( label_text = 'Secs: ', input_width = 75 ) )

    return layout

#---------------------------------#
#-           UTM Input           -#
#---------------------------------#
def utm_input( is_input ):
    
    layout = VBoxLayout()

    layout.add_widget( Label( title = 'Universal Transverse Mercator' ) )

    #  Span layout
    temp_layout = HBoxLayout()
    layout.add_widget( temp_layout )

    #  Column 1:  Grid Zone, and other text inputs
    c1_layout = VBoxLayout()
    temp_layout.add_widget( c1_layout )
    c1_layout.add_widget( Text_Input( label_text = 'Grid Zone: ' ) )
    c1_layout.add_widget( Text_Input( label_text = 'Easting: ' ) )
    c1_layout.add_widget( Text_Input( label_text = 'Northing: ' ) )
    
    #  Column 2:  Hemisphere
    c2_layout = VBoxLayout()
    temp_layout.add_widget( c2_layout )

    c2_layout.add_widget( Check_Box( label_text = 'N', is_active = True ) )
    c2_layout.add_widget( Check_Box( label_text = 'S', is_active = False ) )

    return layout

#---------------------------------#
#-           ECEF Input          -#
#---------------------------------#
def ecef_input( is_input ):
    
    vlayout = VBoxLayout()
    vlayout.add_widget( Label( title = 'Earth-Centered, Earth-Fixed' ) )

    layout = HBoxLayout()
    vlayout.add_widget( layout )

    #--------------------
    #  Input Layout
    clayout = VBoxLayout()
    layout.add_widget( clayout )

    # Text Inputs
    clayout.add_widget( Text_Input( label_text = 'X: ' ) )
    clayout.add_widget( Text_Input( label_text = 'Y: ' ) )
    clayout.add_widget( Text_Input( label_text = 'Z: ' ) )

    #  Radio Inputs
    rlayout = VBoxLayout()
    layout.add_widget( rlayout )

    rlayout.add_widget( Check_Box( label_text = 'm' ) )
    rlayout.add_widget( Check_Box( label_text = 'km' ) )
    
    return vlayout


INPUT_MAP = { TYPE_ECEF:    ecef_input,
              TYPE_GEO_DD:  geo_dd_input,
              TYPE_GEO_DM:  geo_dm_input,
              TYPE_GEO_DMS: geo_dms_input,
              TYPE_UTM:     utm_input }

#--------------------------------------------#
#-          Coordinate Input Menu           -#
#--------------------------------------------#
def build_converter_panel( coord_types ):

    #  Create Page
    page = Page()

    #  Create initial label
    page.add_widget( INPUT_MAP[coord_types[0]]( is_input = True ) )
    page.add_widget( INPUT_MAP[coord_types[1]]( is_input = False ) )

    return page
    

#-------------------------------------------#
#-      Build Geographic Input Menu        -#
#-------------------------------------------#
def build_geographic_input_menu():

    page = Page()

    #  Add Header
    page.add_widget( Header( title = 'Geographic Type',
                             show_time = True ) )
    
    page.add_widget( Label( title = 'Select Input Type' ) )

    page.add_widget( Button( title = 'Decimal-Degrees (d)',
                             hotkey = 'd',
                             retcode = 'geo_dd' ) )
    page.add_widget( Button( title = 'Degree-Minutes (m)',
                             hotkey = 'm',
                             retcode = 'geo_dm' ) )
    page.add_widget( Button( title = 'Degrees-Minutes-Seconds (s)',
                             hotkey = 's',
                             retcode = 'geo_dms' ) )
    page.add_widget( Button( title = 'Exit' ) )
    
    return page



#--------------------------------------------#
#-        Menu for Geographic Coordinate    -#
#--------------------------------------------#
def geographic_input_menu():
    
    page = build_geographic_input_menu()

    #  Run until action received
    while True:

        page.draw()

        #  Check keyboard input
        action = page.check_keyboard()

        if not action is None:
            
            if action == 'exit':
                return action
            elif action == 'geo_dd':
                return TYPE_GEO_DD
            elif action == 'geo_dm':
                return TYPE_GEO_DM
            elif action == 'geo_dms':
                return TYPE_GEO_DMS
            else:
                pass
        else:
            sleep(0.1)

#--------------------------------#
#-      Build Input Menu        -#
#--------------------------------#
def build_input_menu( counter ):

    mode = 'Input'
    if counter == 1:
        mode = 'Output'

    page = Page()

    #  Add Header
    page.add_widget( Header( title = 'Coordinate Conversion',
                             show_time = True ) )
    
    page.add_widget( Label( title = 'Select ' + mode + ' Type' ) )

    page.add_widget( Button( title = 'Geographic (g)',
                             hotkey = 'g',
                             retcode = 'geo' ) )
    page.add_widget( Button( title = 'Earth-Centered, Earth-Fixed (e)',
                             hotkey = 'e',
                             retcode = 'ecef' ) )
    page.add_widget( Button( title = 'Universal Transverse Mercator (u)',
                             hotkey = 'u',
                             retcode = 'utm' ) )
    page.add_widget( Button( title = 'Escape (esc)' ) )

    return page

#---------------------------#
#-      Primary Menu       -#
#---------------------------#
def coord_converter():
    
    coord_types = []

    for x in range( 2 ):

        #  Create fresh page
        page = build_input_menu( x )
        is_first_time = True

        while True:

            page.draw( force_draw = is_first_time )
            is_first_time = False

            #  Check keyboard input
            action = page.check_keyboard()

            if not action is None:

                print( 'Action: ', action )
                if action == 'exit':
                    return
            
                elif action == 'geo':
                    action = geographic_input_menu()
                    if action == 'exit':
                        return
                    coord_types.append( action )
                    break
            
                elif action == 'utm':
                    coord_types.append( TYPE_UTM )
                    break

                elif action == 'ecef':
                    coord_types.append( TYPE_ECEF )
                    break
    
    #  Process Views
    page = build_converter_panel( coord_types )
    is_first_time = True

    while True:

        page.draw( force_draw = is_first_time )
        is_first_time = False

        #  Check keyboard input
        action = page.check_keyboard()

        if not action is None:

            if action == 'exit':
                return
            
                