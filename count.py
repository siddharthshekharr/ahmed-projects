# --------------------------------------------------------------
# 1) Count occurrences
# --------------------------------------------------------------

def count(items, target):

    '''
    This function emulates the list method 'count'. Assume items
    is a list, and target is some object. Return the number of
    times that target appears in items.
    
    YOU MUST USE RECURSION!    
    
    '''


    # Base case: empty list
    if items == []:
        return 0
    
    # Recursive case:
    # Check first element
    if items[0] == target:
        first_count = 1
    else:
        first_count = 0
        
    # recursively count rest of list
    return first_count + count(items[1:], target)


#                 [2, 3, 2, 4, 2]
#                 first_count = 1
#                      +
#                 rest_count →    [3, 2, 4, 2]
#                                first_count = 0
#                                     +
#                                rest_count →    [2, 4, 2]
#                                               first_count = 1
#                                                    +
#                                               rest_count →    [4, 2]
#                                                              first_count = 0
#                                                                   +
#                                                              rest_count →    [2]
#                                                                             first_count = 1
#                                                                                  +
#                                                                             rest_count →    []
#                                                                                            returns 0

# The addition happens bottom-up:
# [] = 0
# [2] = 1 + 0 = 1
# [4, 2] = 0 + 1 = 1
# [2, 4, 2] = 1 + 1 = 2
# [3, 2, 4, 2] = 0 + 2 = 2
# [2, 3, 2, 4, 2] = 1 + 2 = 3