# --------------------------------------------------------------
# 5) Nested list reverser
# --------------------------------------------------------------

def nested_reverse(items):

    '''
    Assume that items is a list, that may contain nested lists
    as elements. This function will perform a reverse operation,
    but with a twist - nested sublists must be reveresed as well.
    
    For example, if the input is [ 1, 2, [5, 4, 3, [9, 0], 3 ] ]
    then you should return [ [ 3, [0, 9], 3, 4, 5], 2, 1 ]

    Hint: You can check if an object is a list by performing the 
    following comparison: type(obj) == list
    
    YOU MUST USE RECURSION!

    '''

    # Base case: if it's not a list, return the item as it is
    if not isinstance(items, list):
        return items
    
    # Recursive case: Reverse the list and call nested_reverse on each element
    reversed_list = []
    for item in items[::-1]: # Reverse the current list
        reversed_list.append(nested_reverse(item))
    return reversed_list

nested_reverse([1, 2, [5, 4, 3, [9, 0], 3]])
|
|-- Step 1: Reverse outer list
|   Original: [1, 2, [5, 4, 3, [9, 0], 3]]
|   Reversed: [[5, 4, 3, [9, 0], 3], 2, 1]
|
|-- Step 2: Process first element [[5, 4, 3, [9, 0], 3]]
|   nested_reverse([5, 4, 3, [9, 0], 3])
|   |
|   |-- Step 2.1: Reverse list
|   |   Original: [5, 4, 3, [9, 0], 3]
|   |   Reversed: [[9, 0], 3, 4, 5]
|   |
|   |-- Step 2.2: Process first element [[9, 0]]
|   |   nested_reverse([9, 0])
|   |   |
|   |   |-- Step 2.2.1: Reverse list
|   |   |   Original: [9, 0]
|   |   |   Reversed: [0, 9]
|   |   |
|   |   |-- Step 2.2.2: Process first element [0]
|   |   |   nested_reverse(0)
|   |   |   Base Case: 0 is not a list → Return 0
|   |
|   |   |-- Step 2.2.3: Process second element [9]
|   |   |   nested_reverse(9)
|   |   |   Base Case: 9 is not a list → Return 9
|   |
|   |   |-- Step 2.2.4: Combine results
|   |   |   [9, 0] → [0, 9]
|   |
|   |-- Step 2.3: Process second element [3]
|   |   nested_reverse(3)
|   |   Base Case: 3 is not a list → Return 3
|   |
|   |-- Step 2.4: Process third element [4]
|   |   nested_reverse(4)
|   |   Base Case: 4 is not a list → Return 4
|   |
|   |-- Step 2.5: Process fourth element [5]
|   |   nested_reverse(5)
|   |   Base Case: 5 is not a list → Return 5
|   |
|   |-- Step 2.6: Combine results
|   |   [5, 4, 3, [9, 0], 3] → [[0, 9], 3, 4, 5]
|
|-- Step 3: Process second element [2]
|   nested_reverse(2)
|   Base Case: 2 is not a list → Return 2
|
|-- Step 4: Process third element [1]
|   nested_reverse(1)
|   Base Case: 1 is not a list → Return 1
|
|-- Step 5: Combine results
|   [1, 2, [5, 4, 3, [9, 0], 3]] → [[3, [0, 9], 3, 4, 5], 2, 1]


