
def get_fibonacci ( digits ):
    sequence = []

    for index in range(digits):
        if ( index > 1 ):
            new_digit = ( index-1 ) + ( index-2 )
            sequence.append( new_digit )
        else:
            sequence.append( index )
    
    return sequence

print ( get_fibonacci(5) )