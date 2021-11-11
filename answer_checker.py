'''

  answer_checker.py

  Author: Daniel Lagesse
  Date: 2021-11-11
  Version: 1

  Answer Checker Component

'''
#-------Libraries-------
import random
import time

#-------Functions-------
def checker():
  score = 0
  print("Here come the questions, remember to press enter when you have typed your answer")
  time.sleep(2)
  for i in range(5): #Loops the question generator 10 times
    num1 = 2
    num2 = 12
    
    answer = num1 * num2 #Defines the answer
    guess = ""
    question = f"\n{num1} x {num2}\n"

    print(question) #Prints the question

    guess = int(input("Please enter the answer (Press Enter once you have typed your answer): "))

    if(guess == answer):
      score += 1
      print(f"The answer is correct! Your score is now {score}")
    else:
      print(f"Incorrect, the answer was {answer}. Your score is now {score}")
    
  return

#-------Main Routine-------
if(__name__ == "__main__"):
  while(True):
    checker()

    prompt = input("Test again? (y/n): ")
    if(prompt.lower() != "y"):
      break