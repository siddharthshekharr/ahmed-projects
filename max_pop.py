# --------------------------------------------------------------
# 2) Maximum population
# --------------------------------------------------------------

def max_pop(items):
    '''
    Assume that items is a list of tuples (country, population).
    Return the country with the largest population.
    Use exception handling to deal with a bad tuple, in which 
    case you return None.

    For example:
    
    max_pop([('China', 1389618778), ('India', 1311559204), ('US', 331883986)])
    would return 'China'

    max_pop([('China'), ('India', 1311559204), ('US', 331883986)])
    would return None, because ('China') is missing the population

    max_pop([('China', 1389618778), ('India', 'lots'), ('US', 331883986)])
    would return None, because 'lots' is not a valid integer

    Do NOT use if/else logic to test the tuple. Use try/except to 
    catch runtime errors if they happen.

    HINT: you do not need to say the type of exception, just say except

    '''

    max_country = None
    # Initialize variable to store country with highest population
    # Start with None as we haven't processed any population yet
    
    max_population = 0
    # Initialize variable to store the highest population found
    # Start with 0 as we haven't processed any populations yet
    
    try:
        # Start try block to catch any possible errors
        
        for country, population in items:
            # Try to unpack each tuple into country and population
            # This will fail if tuple doesn't have exactly 2 elements
            # like in 'China' which would cause a ValueError
            
            if population > max_population:
                # Try to compare populations
                # This will fail if population isn't a valid number
                # like in ('India', 'lots') which would cause a ValueError
                
                max_population = population
                # Update the maximum population found so far
                
                max_country = country
                # Update the country with the maximum population
                
        return max_country
    
    except:
        # If ANY error occurred (unpacking error, comparison error, etc)
        # This catches ALL exceptions, not just specific ones
        
        return None
                
                
            
            
items = [('China', 1389618778), ('India', 1311559204), ('US', 331883986)]

# First iteration: ('China', 1389618778)
#   - population = 1389618778
#   - country = 'China'
#   1389618778 > 0
#   - max_population = 1389618778
#   - max_country = 'China'

# Second Iteration: ('India', 1311559204)
#   - population = 1311559204
#   - country = 'India'
#   1311559204 > 1389618778

# Third Iteration: ('US', 331883986)
#   - population = 331883986
#   - country = 'US'
#   331883986 > 1389618778

# Return 'China'


items = [('India', 1311559204), ('US', 331883986), ('China', 1389618778)]

# First iteration: ('India', 1311559204)
#   - population = 1311559204
#   - country = 'India'
#   1311559204 > 0
#   - max_population = 1311559204
#   - max_country = 'India'

# Second Iteration: ('US', 331883986)
#   - population = 331883986
#   - country = 'US'
#   331883986 > 1311559204

# Third Iteration: ('China', 1389618778)
#   - population = 1389618778
#   - country = 'China'
#   1389618778 > 1311559204
#   - max_population = 1389618778
#   - max_country = 'China'

# Return 'China'