# --------------------------------------------------------------
# 4) Coin counter
# --------------------------------------------------------------

def coins(s) :
    '''
    Assume s is a string representing coins, where q is for 
    quarter, p is for penny, d is for dime, and n is for nickel.

    Return the total amount of money that the string represents.
    
    If the string contains characters that cannot be converted 
    to coins, you should raise a ValueError exception.

    For example, 
    money('ppp') returns 3
    money('pnqqqnd') returns 96
    money('43') raises ValueError

    '''

    total = 0
    
    coin_values = {'p': 1, 'n': 5, 'd': 10, 'q': 25}
    
    for char in s:
        # Loop through each character in the input string
        
        if char not in coin_values:
            # If character isn't a valid coin (p, n, d, q)
            
            raise ValueError
        
        total = total + coin_values[char]
        # Add the value of the current coin to our running total
        
    return total
    # Return the final sum in cents
        



# q (Quarter): 25 cents
# p (Penny): 1 cent
# d (Dime): 10 cents
# n (Nickel): 5 cents