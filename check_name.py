# --------------------------------------------------------------
# 5) Name checker
# --------------------------------------------------------------

def check_name(first, last):

    '''
    Assume first and last are strings. This function should
    check if first and last are valid names. A valid name begins
    with a capital letter, and the rest of the characters are 
    lowercase. 
    
    If the names are valid, return their concatenation in the 
    following form: 'last, first'. For example, if first is
    'Alex' and last is 'Ufkes', return 'Ufkes, Alex'

    If either name is not valid, raise a ValueError exception.
    '''

    if not (first[0].isupper() and first[1:].islower() and last[0].isupper() and last[1:].islower()):
        # Check four conditions
        # 1. first[0].isupper(): first character of first name is uppercase
        # 2. first[1:].islower(): rest of first name is lowercase
        # 3. last[0].isupper(): first character of last name is uppercase
        # 4. last[1:].islower(): rest of last name is lowercase
        # IF ANY of these conditions fail, raise ValueError
        
        raise ValueError
    
    return f'{last}, {first}'
    # If names are valid, return them in format "last, first"
