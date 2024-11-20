# --------------------------------------------------------------
# 1) Numeric string sum
# --------------------------------------------------------------

def sum_words(items):
    '''
    Assume that items is a list of strings, which may or may not
    contain valid integers. For example, one such list might be:
    
    [ '1', '8', 'hello', '3', '5ive', '42'  ] (sum = 54)
    
    This function should return the sum of the integers, without
    crashing on non-digit strings. That is, 'hello' and '5ive'
    in the above example should not cause your function to crash.

    You can use the int() function to parse integer values from
    the strings, but you'll have to use a try/except block to 
    avoid runtime errors when parsing non-integer strings.

    Do NOT use if/else logic to test the strings. Use try/except 
    to catch runtime errors if they happen.

    '''

    total = 0
    # Initialize a variable 'total' to store our running sum
    # We start at 0 since we haven't added any numbers yet
    
    for item in items:
        # Start a loop that will process each string in the items list
        # 'item' will be each individual string in the list, one at a time
        
        try:
            # Begin a "try" block, we'll attempt the code inside this block
            # If it fails, instead of crashing, it will jump to the "excelpt" block
            
            total += int(item)
            # Try to convert the string 'item' to an in teger using int()
            # If successful, add that number to our running total
            # For example: If item is "42", this converts it to 42 and adds it
            
        except ValueError:
            # If int(item) fails because the string isn't a valid integer
            # like "hello" or "5ive", python raises a ValueError
            # This block catches that error
            
            continue
            # Skip this item and continue with the next one in the loop
            # 'continue' means "go to the next iteration of the loop"
            
    return total
            