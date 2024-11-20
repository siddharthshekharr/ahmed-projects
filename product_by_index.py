# --------------------------------------------------------------
# 3) Product by index
# --------------------------------------------------------------

def product_by_index(items, ids) :
    '''
    Assume items is a list of numbers.
    Assume ids is a list of integers.
    This function should return the product of the elements of 
    items at every index in ids
    If either items or ids is empty, return None.

    For example:
    product_by_index([5, 2, 9], [1, 0, 1, 1]) would return 40, 
    since 2 * 5 * 2 * 2 = 40.

    Use exception handling to handle IndexError exceptions
    when the index is out of bounds. In this case, return None.

    For example: 
    productindex([5, 2, 9], [1, 0, 1, 1, 5]) would return None.

    Do NOT use if/else to test index ranges. You should use
    a try/except block.    

    '''

    if not items or not ids:
        # Check if either list is empty
        # This is needed since an empty list would still give a product of 1
        # but the specification wants None for empty lists
        return None
    
    product = 1
    # Initialize the product to 1
    # we'll multiple this by each number we find

    try:
        # Start try block to catch any index out of bounds error

        for index in ids:
            # Loop through each index in the ids list
            
            product = product * items[index]
            # Try to get the item at this index and multiple it
            # This will raise IndexError if index is out of bounds

        return product
        # If we successfully proceessed all indices, return the product
    
    except IndexError:
        return None


product_by_index([5, 2, 9], [1, 0, 1, 1])
items = [5, 2, 9]
ids = [1, 0, 1, 1]

# First iteration: index = 1
#   - items[1] = 2
#   - product = 1 * 2 = 2

# Second iteration: index = 0
#   - items[0] = 5
#   - product = 2 * 5 = 10