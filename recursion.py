# Recursion is a programming concept where a function calls itself to solve a larger problem by breaking it down into smaller, similar subproblems. 

# Key components of recursion:
# 1. Base case: The condition that stops recursion
# 2. Recursive case: The function calling itself with a modified input

def factorial(n):
    # Base case: when n is 0, return 1
    if n == 0:
        return 1
    
    # Recursive case: n * factorial(n - 1)
    else:
        return n * factorial(n - 1)
    
# factorial(4)
# -> 4 * factorial(3)
#         -> 3 * factorial(2)
#                 -> 2 * factorial(1)
#                         -> 1 * factorial(0)
#                                 -> 1

# factorial(4)
-> 24
                               



# factorial(4) -> 4 * factorial(3)

    
    
# Factorial 0 -> 1
# Factorial 1 -> 1
# Factorial 2 -> 2 x 1 = 2
# Factorial 3 -> 3 x 2 x 1 = 6
# Factorial 4 -> 4 x 3 x 2 x 1 = 24
# Factorial 5 -> 5 x 4 x 3 x 2 x 1 = 120
# Factorial 6 -> 6 x 5 x 4 x 3 x 2 x 1 = 720
# Factorial 7 -> 7 x 6 x 5 x 4 x 3 x 2 x 1


# 6 x 5 x 4 x 3 x 2 x 1 -> Factorial 6
# 5 x 4 x 3 x 2 x 1 -> Factorial 5
# 6 x Factorial 5 = Factorial 6

# 7 x 6 x 5 x 4 x 3 x 2 x 1 -> Factorial 7
# 7 x Factorial 6 = Factorial 7