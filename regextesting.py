import re 
import time 
import os

stored_user = []

def Validate_Username(name):
    pattern = re.compile("^[a-z0-9A-z_]{3,10}+$")
    return bool (pattern.match(name))

name = input ("USERNAME :")



def verify_user():
    username = input ("Enter Username: ")
    if re.fullmatch(r"[a-zA-Z0-9_]{3,12}", username):
        print ("Username accepted")
        update_user (username)
    else: 
        print ("Invalid username")
        verify_user()

def update_user