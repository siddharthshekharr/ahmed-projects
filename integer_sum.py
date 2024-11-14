# --------------------------------------------------------------
# 2) Sum of integers
# --------------------------------------------------------------

def integer_sum(items):

    '''
    This function calculates and returns the sum of the integer
    values in the list 'items'.
    
    Be careful - items may contain things other than integers!
    
    For example, if the input is [ 1, 3, 'hello', 5.66 ], you 
    should return 4 (1 + 3).
    
    Hint: You can check if an object is an integer by performing 
    the following comparison: type(obj) == int
    
    YOU MUST USE RECURSION!    
    
    '''


    # Base case: empty list
    if items == []:
        return 0
    
    # Check if first item is an integer
    if type(items[0]) == int:
        first_sum = items[0]
    else:
        first_sum = 0
        
    return first_sum + integer_sum(items[1:])
        


integer_sum([1, 3, 'hello', 5.66])

                       [1, 3, 'hello', 5.66]
                       type(1) == int? Yes
                       first_sum = 1
                          │
                          │ return 1 + integer_sum([3, 'hello', 5.66])
                          ▼
                    [3, 'hello', 5.66]
                    type(3) == int? Yes
                    first_sum = 3
                          │
                          │ return 3 + integer_sum(['hello', 5.66])
                          ▼
                    ['hello', 5.66]
                    type('hello') == int? No
                    first_sum = 0
                          │
                          │ return 0 + integer_sum([5.66])
                          ▼
                         [5.66]
                    type(5.66) == int? No
                    first_sum = 0
                          │
                          │ return 0 + integer_sum([])
                          ▼
                          []
                    Empty list? Yes
                    return 0 (base case)

Now the returns bubble up from bottom to top:

[]                      returns 0
[5.66]                  returns 0 + 0 = 0
['hello', 5.66]         returns 0 + 0 = 0
[3, 'hello', 5.66]      returns 3 + 0 = 3
[1, 3, 'hello', 5.66]   returns 1 + 3 = 4

Final Result: 4