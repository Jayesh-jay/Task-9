'''
a)Email address
'''
import re

def is_valid_email(email):
    # Define a simple regular expression for email validation
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    match = re.match(email_pattern, email)
    
    # Return True if the email is valid, False otherwise
    return bool(match)

email_to_validate = (input())
if is_valid_email(email_to_validate):
    print(f"{email_to_validate} is a valid email address.")
else:
    print(f"{email_to_validate} is not a valid email address.")
    


'''
b) mobile numbers of bangladesh
'''
import re

# Define a regex pattern for mobile numbers of Bangladesh
mobile_pattern = r"^(?:\+880|0)\d{10}$"

# Define a function that checks if a given string matches the mobile pattern
def validate_mobile_bd(mobile):
    # Use the re.match() function to check for a match
    match = re.match(mobile_pattern, mobile)
    # Return True if there is a match, False otherwise
    return bool(match)

# Test the function
print(validate_mobile_bd(input()))  



'''
c)Telephone numbers of USA
'''
import re

def validate_usa_telephone_number(number):
    # Define a simplified regular expression pattern for US telephone numbers
    pattern = re.compile(r'^\(\d{3}\) \d{3}-\d{4}$')

    # Return True if the input number matches the pattern, otherwise False
    return bool(pattern.match(number))

# Example usage:

print(validate_usa_telephone_number(input())) 



'''
d)16 character alpha-numeric password composed of alphabets of upper case,lower case,special character,numbers
'''

import re

def validate_password(password):
    # Define the regular expression pattern
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{16}$')

    # Return True if the password matches the pattern, otherwise False
    return bool(re.match(pattern, password))

# Example usage:
print(validate_password(input()))
