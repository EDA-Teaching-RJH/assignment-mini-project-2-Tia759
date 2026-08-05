import re 

def Validate_Username(username):
    pattern = re.compile("[a-z0-9A-z_]{3,10}")
