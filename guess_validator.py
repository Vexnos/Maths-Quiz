'''
--------------------------------------------------------------------
  guess_validator.py

   Project: Multiplication Maths Quiz
  Standard: 91883 & 91884
    School: Mountainview Highschool
    Author: Daniel Lagesse
      Date: 2021-11-11
   Version: 1
    Python: 3.9.4

  Guess Validator Component
--------------------------------------------------------------------
'''
#-------Libraries-------
import random #Imports the random library which allows the program to generate random numbers for the question

#-------Functions-------
#This is the guess validator, it ensures the user cannot enter an invalid value as their answer to the question (This function is designed to work within the answer checker function)
def guess_validator():
  global guess #Makes the user's guess global so other functions can use it
  example_question = "\n2 x 3\n" #This is test code and will be removed in the final version
  while(True): #Loops to ensure that an invalid value cannot be stored
    try:
      guess = int(input("Please type the answer here (press enter afterwards): "))
    except ValueError:
      print("Invalid value entered, please try again")
      print(example_question) #example_question will be replaced with the question variable in the final quiz
      #Prints the question again so the user doesn't have to scroll up
      continue
    print(f"guess = {guess}")
    break

  return

#-------Main Routine-------
if(__name__ == "__main__"):
  while(True):
    guess_validator()

    prompt = input("Test again? (y/n): ") # Test Code
    if(prompt.lower() != "y"):
      break