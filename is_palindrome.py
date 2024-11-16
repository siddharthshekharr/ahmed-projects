# --------------------------------------------------------------
# 4) Palindrome checker
# --------------------------------------------------------------

def is_palindrome(text):

    '''
    A recursion classic.
    
    Assume that 'text' is a string. Return True if text is a 
    palindrome, and False otherwise. 
    
    A string is a palindrome if it reads the same forwards and
    backwards. For example, 'racecar' is a palindrome.
    
    YOU MUST USE RECURSION!

    '''

    # Base case
    if len(text) <= 1:
        return True
    
    # Recursive case: Check the substring without the first and last characters
    return (text[0] == text[-1]) and is_palindrone(text[1:-1])

text = "apple"
text[1:-1] -> "ppl"