import re 


def Validate_Username(username):
    pattern = re.compile("^[a-z0-9A-z]{3,10}$")
    return bool (pattern.match(username))

name = input ("USERNAME :")

print (Validate_Username('name'))