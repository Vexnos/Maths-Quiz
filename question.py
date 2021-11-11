'''

  question.py

  Author: Daniel Lagesse
  Date: 2021-11-03
  Version: 1

  Question Generator Component

'''

#-------Libraries-------
import random
import time

#-------Functions-------
def question():
  start = time.time() #Starts the timer
  score = 0
  print("Here come the questions, remember to press enter when you have typed your answer")
  time.sleep(2)
  for i in range(5): #Loops the question generator 10 times
    num1 = random.randint(n1,n2) #Generates a random number using the factors from the diff() function
    num2 = random.randint(n1,n2)
    
    answer = num1 * num2 #Defines the answer
    guess = ""
    question = f"\n{num1} x {num2}\n"

    print(question) #Prints the question

  stop = time.time()
  user_time = stop-start

  print(f"\nscore of {score}, time = {user_time:.2f}s\n") # TODO: add an actual sentence here
  #Displays the user's time to 2 significant figures

  return

#-------Main Routine-------
if(__name__ == "__main__"):
  while(True):
    n1 = 1
    n2 = 12
    question()

    prompt = input("Test again? (y/n): ")
    if(prompt.lower() != "y"):
      break