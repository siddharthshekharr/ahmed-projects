def divide(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        print("There was an error dividing the number with 0")
        
def divide(a, b):
    try:
        # Early Problem Detection
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        else:
            c = a / b
    except ZeroDivisionError as a:
        print("There was an error dividing the number with 0", a)
    
    
divide(10, 0)



def send_email(email_address):
    if '@' not in email_address:
        raise ValueError("Invalid email address")
    
send_email("sfsg")