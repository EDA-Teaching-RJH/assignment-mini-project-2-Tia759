import re
import time 
import os 

colour = ["green","red","Brown","purple","pink"]

stored_user = []

def verify_user():
    username = input ("Enter Username: ")
    if re.fullmatch(r"[a-zA-Z0-9_]{3,12}", username):
        print ("Username accepted")
        time.sleep(1)
        update_user (username)
    else: 
        print ("Invalid username")
        time.sleep(1)
        verify_user()

def update_user(username):
    stored_user.append(username)

verify_user()

from Testingimport import random_colour