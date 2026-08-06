import re 


def Validate_Username(name):
    pattern = re.compile("^[a-z0-9A-z_]{3,10}$")
    return bool (pattern.match(name))

name = input ("USERNAME :")

print (Validate_Username('name'))
