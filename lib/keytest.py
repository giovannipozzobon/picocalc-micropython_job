
#  Project Libraries
import turtle

def run( verbose = False ):
    '''
    Run the keyboard logger
    '''
    
    okay_to_run = True
    while okay_to_run:

        # Check for keyboard input
        keys = turtle.check_keyboard( verbose = verbose )
        if len(keys) > 0:
            for key in keys:
                
                #. Get the mapped key
                print( 'Detected: ', key, ', Key: ', turtle.Key.to_key( key ) )

                if key == turtle.Key.ESCAPE:
                    print('Exiting Application')
                    okay_to_run = False
                    break


