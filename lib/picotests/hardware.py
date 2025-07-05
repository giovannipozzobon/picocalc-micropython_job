
# Micropython Libraries
import logging
import sys
import time

#  Project Libraries
import picocalc.colors as colors
import picocalc.core as pico
import turtle


def run_full( log_level = logging.DEBUG, log_path = './hardware.log' ):

    #  Setup Logger
    if not log_path is None:
        logging.basicConfig( level    = log_level,
                             filename = log_path )
    else:
        logging.basicConfig( level = log_level )
    logging.info( 'Logging initialized' )

    #  Setup the Turtle Display
    screen = turtle.init()
    screen.fill( colors.GS4.BLACK )
    screen.wait_update_finished()

    # Draw Header
    screen.fill_rect( 10, 10, 300, 20, colors.GS4.LIGHT_GRAY )
    screen.draw_text( "Hardware Test", 10, 20, colors.GS4.BLACK )
    
    # Menu
    okay_to_run = True
    while okay_to_run:

        screen.fill_rect( 10, 30, 300, 280, colors.GS4.GRAY )
        screen.draw_text( "Status Information:", 10, 40, colors.GS4.GREEN )

        screen.draw_text( " - Battery Status    : " + str(int(pico.keyboard.battery())),            10, 60, colors.GS4.GREEN )
        screen.draw_text( " - Screen Backlight  : " + str(pico.keyboard.backlight()),          10,  80, colors.GS4.GREEN )
        screen.draw_text( " - Keyboard Backlight: " + str(pico.keyboard.backlight_keyboard()), 10,  100, colors.GS4.GREEN )
        

        screen.draw_text( "> Select Option: ", 10, 270, colors.GS4.GREEN )

        #. Get keyboard status
        keys = turtle.check_keyboard()
        
        for key in keys:
            if key == turtle.Key.ESCAPE:
                screen.draw_text("Hello PicoCalc!", 10, 310, 15, colors.GS4.GREEN )
                break
    
        time.sleep(0.1)


    screen.reset()
    logging.info( "Exiting Application" )

def run( log_level = logging.DEBUG, log_path = './hardware.log'  ):

    try:
        run_full( log_level, log_path )
    except Exception as e:
        turtle.reset()
        logging.error( 'Exception caught: ', e )
