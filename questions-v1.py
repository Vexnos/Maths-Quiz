'''
--------------------------------------------------------------------
  questions-v1.py

   Project: Multiplication Maths Quiz
  Standard: 91883 & 91884
    School: Mountainview Highschool
    Author: Daniel Lagesse
      Date: 2021-11-03
   Version: 1
    Python: 3.9.4

  Question Generator Component v1
--------------------------------------------------------------------
'''
#-------Libraries-------
import random #Imports the random library which allows the program to generate random numbers for the question
import time #Imports the time library which allows the program to slow down the interval between actions and allows the quiz to be timed

#-------Functions-------
def question():
  global questions, score, guess, answers #Makes these variables global so other functions can access them
  score = 0 #Sets the score to 0 each time the quiz is activated
  start = time.time() #Starts the timer
  questions = ["2 x 3",
               "4 x 5",
               "7 x 8",
               "12 x 11",
               "7 x 10",
               "8 x 4",
               "3 x 9",
               "5 x 5",
               "4 x 9",
               "12 x 12"] #Stores the questions in a list

  answers = [6, 20, 56, 132, 70, 32, 27, 25, 36, 144] #Stores the answers in a list

  for i in range(10): #Loops the question generator 10 times
    print(questions[i]) #Prints an item from the questions list per iteration
    guess = "" #Sets the guess variable to nothing so the previous guess doesn't conflict
    while(True): #Loops the guess try/except checker in case the user enters an invalid value
      try:
        guess = int(input("\nPlease enter the answer: ")) #This is where the user enters their answer
      except ValueError: 
        print("Invalid value, please try again\n")
        print(questions[i])
        continue #Continues the loop to its next iteration
      break #Breaks the loop if there is no value error with the answer

    check(i) #Calls the check function per question

  stop = time.time() #Stops the timer
  user_time = stop - start

  print(f"The quiz is over! You got a score of {score} in a time of {user_time:.2f}")

#This is the check function, it will check if the user's guess matches up with the answer, if not a point is revoked (cannot go below 0). If they do match, a point is given
def check(num):
  global score
  if(guess == answers[num]):
    score += 1 #Adds a point
    print(f"Correct! Your score is now {score}\n")
  else:
    if(score <= 0): #Checks that the score cannot be negative
      score = 0
      print(f"Incorrect, the answer was {answers[num]}, your score is now {score}\n")
    else:
      score -= 1 #Revokes a point
      print(f"Incorrect, the answer was {answers[num]}, your score is now {score}\n")

#-------Main Routine-------
if(__name__ == "__main__"):
  while(True):
    question() #Calls the question function

    prompt = input("Test again? (y/n): ") #Test code
    if(prompt.lower() != "y"):
      quit()
