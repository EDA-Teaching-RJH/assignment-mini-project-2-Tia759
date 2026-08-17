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
#short lines and delayed paragrah used to improve readablity for users

while True: 
    #while true used (as oppsed to if/else functions) to create a loop so that i could use the break function to end the code
    if choice == 1:
         print ("Hello", stored_user) 
         time.sleep(1)
         print ("You will now recieve a random colour.\n I am then going to ask you some questions\n Please type 1 for Yes and 2 for No.\n Your colour is...")
         time.sleep(1)
         Colour = random.choice (["green","red","Brown","purple","pink"])
         print (Colour)
         Guess_one = int(input("Is your colour a primary colour?\n Yes = 1\n No = 2"))
         #before i specified Guess_one to be an integer it would not run the if feature and would ignore it. And move straight onto Guess_two.
         if Guess_one == 1:
             from results import result
             result() #imported from a libary i created. It asks if the users colour is red and then tells them who won
             break
         else: 
             colour.pop (1) #removes red from the list of colours
             Guess_two = int(input("Is your colour associated with nature?\n Yes = 1\n No = 2"))
             if Guess_two == 1:
                 from results import result_2
                 result_2() #it asks if the users colour is brown and specifys if they win or not
             else:
                 from results import results_3
                 results_3()# asks if the users colour is pink
                 #Guess_two only asks about brown or pink to include a chance for the user to lose if they got purple or green
         break
    elif choice == 2:
        print ("Your username is", stored_user)
        break
    else: 
        #need to make this into an 'elif' function so that it will only run when '3' is inputed
        print ("Showing Previous players Scores:")
        time.sleep(1)
        from file_handeler import reading_results
        reading_results()
        #reads a csv file. Using https://www.youtube.com/watch?v=raRt1SeqpK4 i learnt that 'r' stands for read. 'a' stands for append and 'w' stands for write when writing csv code.
        break
    #attempted to give the user the ability to add themselves to the csv list however data_row kept coming up as undefined 
    

