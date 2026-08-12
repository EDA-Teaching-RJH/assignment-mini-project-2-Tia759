import re
import time 
import os 
import random


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

choice = int(input("MENU\n 1.New Game\n 2.User Information\n 3.Previous Games Information\n"))
time.sleep(1)

while True: 
    if choice == 1:
         print ("Hello", stored_user) 
         time.sleep(1)
         print ("You will now recieve a random colour.\n I am then going to ask you some questions\n Please type 1 for Yes and 2 for No.\n Your colour is...")
         time.sleep(1)
         Colour = random.choice (["green","red","Brown","purple","pink"])
         print (Colour)
         Guess_one = int(input("Is your colour a primary colour?\n Yes = 1\n No = 2"))
         if Guess_one == 1:
             from results import result
             result()
             break
         else: 
             colour.pop (1)
             Guess_two = int(input("Is your colour associated with nature?\n Yes = 1\n No = 2"))
             if Guess_two == 1:
                 from results import result_2
                 result_2()
         break
    else:
        print ("placeholder")
        break
    

