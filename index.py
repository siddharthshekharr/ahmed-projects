def largest_diff(items):
    '''
    This first question is very simple, and is intended to convey 
    the spirit behind the challenge modes.

    Assume that items is a list of integers. Find and return the 
    largest possible difference between any two values in the list.
    
    AMATEUR HOUR:

    Using a nested loop, calculate the difference between every
    possible pair of values. Return the largest.

    CHALLENGE MODE: 
    
    Avoid nested loops. Avoid writing your own loops entirely
    in favor of using two calls to built-in Python functions.
    This function can be solved with a single line of code.
    '''
    items = [1, 5, 2, 9, 3]
    max_diff = 0
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            # Calculate absolute difference
            diff = abs(items[i] - items[j])
            
            # Update max_diff if we found a bigger difference
            max_diff = max(0, 4)
    return max_diff
    

First iteration (i = 0):
    j = 1: Compare 1 with 5 -> |1-5| = 4 (max_diff becomes 4)
    j = 2: Compare 1 with 2 -> |1-2| = 1 (max_diff stays 4)
    j = 3: Compare 1 with 9 -> |1-9| = 8 (max_diff becomes 8)
    j = 4: Compare 1 with 3 -> |1-3| = 2 (max_diff stays 8)
    
Second iteration (i = 1):
    j = 2:
    j = 3:
    j = 4:

Third Iteration (i = 2)
    j = 3:
    j = 4:
        
Fourth Iteration (i = 3):
    j = 4:
    
    


for i in range(5):
    print(i)
    
max(3, 100)
max(1, 2)
max(3, 7)