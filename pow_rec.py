# --------------------------------------------------------------
# 3) Exponentiation
# --------------------------------------------------------------

def pow_rec(base, exponent):

    '''
    Assume that base and exponent are integers >= 0.
    
    Calculate and return base to the power of exponent using 
    repeated multiplications.
    
    YOU MUST USE RECURSION!

    '''

    # Base case
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
        
    
    # Recursive case
    return base * pow_rec(base, exponent - 1)
        
        
                    pow_rec(2, 3)
                    exponent != 0 or 1
                    return 2 * pow_rec(2, 2)
                          │
                          ▼
                    pow_rec(2, 2)
                    exponent != 0 or 1
                    return 2 * pow_rec(2, 1)
                          │
                          ▼
                    pow_rec(2, 1)
                    exponent = 1
                    return 2 (base case)

Now multiply back up:
pow_rec(2, 1) returns 2
pow_rec(2, 2) returns 2 * 2 = 4
pow_rec(2, 3) returns 2 * 4 = 8

Final result: 8


2^3 = 2 * 2 * 2

pow_rec(2, 3) means 2^3
- 2^3 = 2 * 2^2


2^3 = 2 * 2 * 2
2^2 = 2 * 2

2^3 = 2^1 * 2^2







2^7 = 2^1 * 2^6



a^b * a^c = a^(b+c)

2^1 * 2^2 = 2^3