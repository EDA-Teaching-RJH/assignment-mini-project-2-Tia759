from Testingimport import random_colour 
from Testingimport import result 
from Testingimport import result_2
from Testingimport import result_3
from regextesting import verify_user
from regextesting import update_user
import re

colour = ["green","red","Brown","purple","pink"]



choice = input ("MENU\n 1.New Game\n 2.User Information\n 3.Previous Games Information\n")

if choice := 1: 
    print ("Hello" , name) 
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



