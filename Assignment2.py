from Testingimport import random_colour 
from Testingimport import result 
from Testingimport import result_2
from Testingimport import result_3
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

choice = input ("MENU\n 1.New Game\n 2.User Information\n 3.Previous Games Information\n") 
time.sleep(1)

if choice := 1: 
    print ("Hello" stored_user) 
    print ("You will now receive a random colour. I am then going to ask you some questions.Please type 1 for yes and 2 for no.\nYour colour is...")
    random_colour()
    Guess_one = input ("Is your colour a primary colour? 1=yes 2=no")
    if Guess_one == 2: 
        colour.pop(1)
        print (colour)
        Guess_two = input ("Is your colour associated to nature? 1=yes 2=no")
        if Guess_two == 1:
            colour.pop (2,3)
            result_2()
            

        if Guess_two == 2:
            colour.pop (0,1)
            result_3()


    else:
        print (colour)
    
    
        

else:
 print ("placeholder")



