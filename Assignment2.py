from Testingimport import random_colour 

name = input ("What is your name?")

choice = input ("MENU\n 1.New Game\n 2.User Information\n 3.Previous Games Information\n")

if choice := 1: 
 print ("Hello" , name) 
 print ("You will now receive a random colour. I am then going to ask you some questions.\nYour colour is...")
 random_colour()
 Guess_one = input ("Is your colour a primary colour?")
 

else :
 print ("AAAAA")



