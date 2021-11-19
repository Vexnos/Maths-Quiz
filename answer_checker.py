'''
--------------------------------------------------------------------
  answer_checker.py

   Project: Multiplication Maths Quiz
  Standard: 91883 & 91884
    School: Mountainview Highschool
    Author: Daniel Lagesse
      Date: 2021-11-11
   Version: 1
    Python: 3.9.4

  Answer Checker Component
--------------------------------------------------------------------
'''
#-------Libraries-------
import random #Imports the random library which allows the program to generate random numbers for the question
import time #Imports the time library which allows the program to slow down the interval between actions and allows the quiz to be timed

#-------Functions-------
#This is the answer checker, it checks if the user's guess is the same as the answer, if it is, the user gains a point, if not, a point is revoked (This function is designed to work within the question function)
def answer_checker():
  global score
  #-------Code for Testing-------
  score = 0
  print("Here come the questions, remember to press enter when you have typed your answer")
  time.sleep(2)
  for i in range(5): #Loops the question generator 5 times
    num1 = random.randint(n1,n2)
    num2 = random.randint(n1,n2)
    
    answer = num1 * num2 #Defines the answer
    guess = ""
    question = f"\n{num1} x {num2}\n"

    print(question) #Prints the question

    #---------------------------------------

    guess = int(input("Please enter the answer (Press Enter once you have typed your answer): "))

    if(guess == answer):
      score += 1 #Adds 1 point to the score
      print(f"The answer is correct! Your score is now {score}")
    else:
      score -= 1 #Revokes a point from the score if score is above 0
      print(f"Incorrect, the answer was {answer}. Your score is now {score}")
    
  return

#-------Main Routine-------
if(__name__ == "__main__"):
  while(True):
    n1 = 1
    n2 = 12
    answer_checker()

    prompt = input("Test again? (y/n): ") # Test Code
    if(prompt.lower() != "y"):
      break