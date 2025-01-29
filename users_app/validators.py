
from django.core.exceptions import ValidationError
import re

def match_regex(rcv_regex, rcv_str):
    """
    This method uses the re.match method
    Args:
        rcv_regex: Datatype, r_string with regex pattern
        rcv_str: Datatype, string to conduct regex with
    Returns Boolean True/False
    """
    if re.match(rcv_regex, rcv_str) == None:
        return False
    else:
        return True


def validate_name_format(name):
    """ Only accepts string in the following format <Uppercase Letter, followed by Lowercase letters """
    print(name)
    # Regex for accepted name structure
    regex = r"^[A-Z][a-z]+"
    #err_msg = "Invalid naming convention for name [%(name)s]"
    err_msg = 'Name format must be "An Uppercase letter following by lowercase letters"'
    
    if match_regex(regex, name):
        return name
    else:
        #print 
        raise ValidationError(err_msg, params={'name': name})

def validate_email(email):
    """ Only accepts string ending with "@<letters>.com" """
    print(email)
    regex = r'^[\w]+@[\w]+\.com' # Regex for email acceptance
    err_msg = "Email must be in proper format"
    
    if match_regex(regex, email):
        return email
    else:
        #print 
        raise ValidationError(err_msg, params={'email': email})


#TODO: REMVOE BELOW WHEN DONE WITH DEV
if __name__ == "__main__":  
    validate_email('my_email@loco.com') # Pass
    #validate_email('my email@.com') # Fail
    #validate_email('myemail@@.com') # Fail
    #validate_email('myemail@loco.net') # Fail
    #validate_name_format('aNt') #Fail
    #validate_name_format('NAme') #Fail
    validate_name_format('Testing') # Pass


