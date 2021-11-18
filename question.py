'''
--------------------------------------------------------------------
  question.py

   Project: Multiplication Maths Quiz
  Standard: 91883 & 91884
    School: Mountainview Highschool
    Author: Daniel Lagesse
      Date: 2021-11-03
   Version: 1
    Python: 3.9.4

  Question Generator Component
--------------------------------------------------------------------
'''
#-------Libraries-------
import random #Imports the random library which allows the program to generate random numbers for the question
import time #Imports the time library which allows the program to slow down the interval between actions and allows the quiz to be timed

#-------Functions-------
#This is the question generator, it will generate 10 random questions using the factors from the diff() function.
def questions():
  global question, answer, guess, score
  score = 0 #Sets the score to 0 every time the program is activated.
  print("\nHere come the questions, remember to press enter when you have typed your answer")
  time.sleep(2)
  start = time.time() #Starts the timer and stores the recorded time in a variable
  for i in range(3): #Loops the question generator 10 times
    num1 = random.randint(n1,n2) #Generates a random number using the factors from the diff() function
    num2 = random.randint(n1,n2)
    
    answer = num1 * num2 #Defines the answer
    guess = ""
    question = f"\n{num1} x {num2}\n"

    print(question) #Prints the question

  stop = time.time() #Stops the timer and stores the recorded time in a variable
  user_time = stop-start #Subtracting the start time from stop time allows us to find the user's time.

  print(f"You got a score of {score}/10 in a time of {user_time:.2f}s") #{user_time:.2f} Displays the user's time to 2 significant figures

  return

#-------Main Routine-------
if(__name__ == "__main__"):
  while(True):
    n1 = 1 #These are test factors and will not be in the actual quiz
    n2 = 12
    questions() #Calls the questions function

    prompt = input("Test again? (y/n): ")
    if(prompt.lower() != "y"):
      break