# --------------------------------------------------------------
# 6) Integers from iterators
# --------------------------------------------------------------

def get_next_int(it):

    ''' 
    Assume that 'it' is an iterator, NOT a list/sequence. Given
    the iterator, this function returns the next integer value
    produced by the iterator.

    If the iterator runs out of elements, and cannot produce 
    another integer, return None.

    Hint: Use the next() function to get elements, and be sure 
    to catch the StopIteration error when it occurs. 

    '''
    try:
        # Try to do two things that might fail
        
        # 1. Get next value from iterator
        # This might raise StopIteraion if iterator is exhausted
        value = next(it)
        
        
        # 2. Convert value to integer
        # This might raise ValueError if value isn't convertible to int
        return int(value)
    
    except (StopIteration, ValueError):
        return None
        

iter1 = iter(['1', '2', '3'])

get_next_int(iter1)