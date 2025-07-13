#  This does a test of the logging API

#  Micropython Libraries
import logging

logging.basicConfig( level = logging.DEBUG )

def test_logger():
    
    l = logging.getLogger('foo')
    l.setLevel( logging.DEBUG )
    l.debug( f'Test {1}, {"hi!"}' )
    
    print( 'Message To User!' )
    print( '  1.  Do you see a log message saying "Test 1, hi!" ?' )
    print( '  2.  Is this message DEBUG?' )
    print( '  3.  Do you see a timestamp?' )

    
    
test_logger()
    