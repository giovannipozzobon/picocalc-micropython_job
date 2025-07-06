
#  Micropython Libraries
import logging
import os
import sys
import time

#  Project Libraries
from colorer import Back
import picocalc.colors as pcolors
import turtle

class Folder:

    def __init__(self, cdir):
        self.cdir = cdir

    def current_path(self):
        return self.cdir

    def list_contents(self):
        return os.listdir( self.cdir )


def run_full( cdir = '.', log_level = logging.DEBUG, log_path = './browser.log' ):
    
    #  Setup Logger
    if not log_path is None:
        logging.basicConfig( level    = log_level,
                             filename = log_path )
    else:
        logging.basicConfig( level = log_level )
    logging.info( 'Logging initialized' )

    #  Current Directory
    folder = Folder( cdir )

    #  Setup the Turtle Display
    screen = turtle.init()
    screen.fill( pcolors.GS4.BLACK )
    screen.wait_update_finished()

    #  Limits
    max_row = 300
    text_row_height = 15

    okay_to_run = True
    while okay_to_run:

        #. Populate Header
        screen.fill_rect( 10, 10, 300, 20, pcolors.GS4.GRAY )
        screen.draw_text( "PicoCalc Filesystem Browser", 10, 20, pcolors.GS4.GREEN )
        screen.wait_update_finished()
        
        #  Get content
        file_list = folder.list_contents()

        #  Show Content
        cur_row = 50
        c = [ Back.RED, Back.GREEN, Back.YELLOW, Back.BLUE, Back.MAGENTA, Back.CYAN ]
        for i in range( len( file_list ) ):
            idx = i + 1
            screen.fill_rect( 10, cur_row - text_row_height, 200, text_row_height, c[i % len(c)] )
            screen.draw_text( '{}: {}'.format( i, file_list[i] ), 
                              30, cur_row, 
                              pcolors.GS4.LIGHT_GRAY )
            cur_row += text_row_height

            if cur_row > max_row:
                break
        
        # Draw Footer
        screen.fill_rect( 0, 300, 320, 20, pcolors.GS4.GRAY )
        screen.draw_text( '{}'.format( folder.current_path() ), 20, 320, pcolors.GS4.LIGHT_GRAY )

    
        # Check for keyboard input
        #keys = turtle.check_keyboard()

        #for key in keys:
        #    if key == turtle.Key.ESCAPE:
        #        screen.fill( pcolors.GS4.BLACK )
        #        screen.draw_text("Exiting!", 10, 310, pcolors.GS4.GREEN )
        #        okay_to_run = False
        #        break
        #
        #time.sleep(0.2)
        time.sleep(5)
        okay_to_run = False

    #  Put everything back
    screen.reset()

    logging.debug( 'Exiting Application' )
    

#----------------------------------------#
#-          Run The Application         -#
#----------------------------------------#
def file_browser( cdir      = '.',
                  log_level = logging.DEBUG,
                  log_path  = './browser.log'  ):

    try:
        run_full( cdir, log_level, log_path )
    
    except Exception as e:
        turtle.reset()
        print('EXCEPTION')
        sys.print_exception( e )
        logging.error( 'Exception caught: {}'.format(e) )
        sys.print_exception( e )

