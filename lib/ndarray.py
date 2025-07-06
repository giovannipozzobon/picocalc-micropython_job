#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#
#*                                                                                    *#
#*                           Copyright (c) 2025 Terminus LLC                          *#
#*                                                                                    *#
#*                                All Rights Reserved.                                *#
#*                                                                                    *#
#*          Use of this source code is governed by LICENSE in the repo root.          *#
#*                                                                                    *#
#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#


class array:

    def __init__( self, 
                  indata,
                  dtype = float ):
        
        self.data  = None
        self.shape = None

        #  If the input is a list, it's "data"
        if isinstance(indata,list):
            self.data = indata
        
        #  If the input is a tuple, it's the shape
        elif isinstance(indata,tuple):
            self.shape = indata

        #  If it's an array, we're copying it
        elif isinstance(indata,array):
            self.shape = indata.shape
            self.data  = indata.data
            self.dtype = indata.dtype

        else:
            raise Exception( 'Not sure what the input is?' )
        
        #  If the input was a shape, create a zero-array from the
        #  shape
        if self.data is None:
            self.data = []

            def create_zero_array( dims ):
                if not dims:
                    return 0
                return [ create_zero_array( dims[1:] ) for _ in range( dims[0] ) ]
            self.data = create_zero_array( list( self.shape ) ) 

        #  If the input was data, then compute the shape    
        if self.shape is None:
            self.shape = self.get_shape()
        self.dtype = float

    def __getitem__( self, *args ):
        
        def access( data, args ):
            
            if isinstance(args,int):
                return data[args]
            
            if len(args) == 1:
                return data[args[0]]
            return access( data[args[0]], args[1:] )

        return access( self.data, args[0] )
    

    def __setitem__( self, index, newvalue ):

        def setval( data, idx, newval ):
            if isinstance( idx, int ):
                data[idx] = newval
            elif isinstance( idx, tuple ) and len(idx) == 1:
                data[idx[0]] = newval
            else:
                setval( data[idx[0]], idx[1:], newval )
        
        setval( self.data, index, newvalue)
        

    def __add__( self, other ):

        assert( len( self.shape ) == len( other.shape ) )
        for x in range( len( self.shape ) ):
            assert( self.shape[x] == other.shape[x] )

        def add_vals( val1, val2 ):
            if isinstance( val1, list ):
                return [ add_vals( val1[x], val2[x] ) for x in range( len( val1 ) ) ]
            return val1 + val2

        return array( add_vals( self.data, other.data ),
                      dtype = self.dtype )
    
    def __sub__( self, other ):

        assert( len( self.shape ) == len( other.shape ) )
        for x in range( len( self.shape ) ):
            assert( self.shape[x] == other.shape[x] )

        def sub_vals( val1, val2 ):
            if isinstance( val1, list ):
                return [ sub_vals( val1[x], val2[x] ) for x in range( len( val1 ) ) ]
            return val1 - val2

        return array( sub_vals( self.data, other.data ),
                      dtype = self.dtype )

    def __mul__( self, other ):

        if isinstance( other, float ) or isinstance( other, int ):
            def mult_vals( value, other ):
                if isinstance( value, list ):
                    return [ mult_vals( value[x], other ) for x in range( len( value ) ) ]
                return value * other
            return array( mult_vals( self.data, other ),
                          dtype = self.dtype )
        raise Exception('Not Implemented Yet')
    

    def get_shape( self ):

        def temp_shape( arr ):
            if isinstance(arr, list) and arr:  # Check if it's a non-empty list
                return [len(arr)] + temp_shape(arr[0])  # Recurse into the first element
            return []  # Base case: Return empty list when a non-list item is encountered
        return tuple(temp_shape( self.data ))

    def __str__( self ):

        output = '[ '
        offset = ' '
        for r in range( len( self.data ) ):

            #  Check if the list 
            if isinstance( self.data[r], list ):
                offset += '  '
                if r != 0:
                    output += ' '
                for c in range( len( self.data[r] ) ):
                    output += '[ '
                    output += "{0}".format( self.data[r][c] )
                    output += ' ],'

                output += '\n'
                offset = offset[:-2]

            else:
                output += "{0}".format( self.data[r] )
                if r < len(self.data)-1:
                    output += ','

        output += ' ]'
        return output
    
    def clone(self):

        return array( self.data[:], self.dtype )
    
def zeros( dims, dtype = float ):
    '''
    Build a matrix with zeros
    '''
    data = []
    for r in range( dims[0] ):
        data.append( [] )
        for c in range( dims[1] ):
            data[r].append( dtype(0) )
    return array( data, dtype = dtype )

def eye( dims, dtype = float ):
    '''
    Build a matrix with the identity
    '''
    data = []
    for r in range( dims[0] ):
        data.append( [] )
        for c in range( dims[1] ):
            if r == c:
                data[r].append( dtype( 1 ) )
            else:
                data[r].append( dtype( 0 ) )
    return array( data, dtype = dtype )

def mat_mul( matA, matB ):
  dshape = (matA.shape[0],
          matB.shape[1])
  
  output = zeros( shape = dshape ) 
  
  for i in range(matA.shape[0]):
    for j in range(matB.shape[1]):
      sum = 0
      for k in range(matA.shape[1]):
        sum += matA[i,k] * matB[k,j]
      output[i,j] = sum
      
  return output
  
def dot( val1, val2 ):
    
    if isinstance(val1,array):
        return val1 * val2
    elif isinstance(val2,array):
        return val2 * val1
        
