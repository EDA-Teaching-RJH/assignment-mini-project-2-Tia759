import re
import time 
import os 
import random


# colour.pop removes colours from this list 
colour = ["green","red","Brown","purple","pink"]

stored_user = []

def verify_user():
    username = input ("Enter Username: ")
    #code is 3-12 digits long so that people can choose between putting their real name or a fake username
    if re.fullmatch(r"[a-zA-Z0-9_]{3,12}", username):
        print ("Username accepted")
        time.sleep(1)
        #time.sleep function used to immitate a computer processing something 
        update_user (username)
    else: 
        print ("Invalid username")
        time.sleep(1)
        verify_user()
        #if the username is invalid it restarts the function so that the user doesn't have to run the code again

def update_user(username):
    stored_user.append(username)
#stores the username as it will be printed out again
#this function runs within the verify_user() function 

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
             else:
                 from results import results_3
                 results_3()
         break
    elif choice == 2:
        print ("Your username is", stored_user)
        break
    else: 
        print ("Showing Previous players Scores:")
        time.sleep(1)
        from file_handeler import reading_results
        reading_results()
        break
    

