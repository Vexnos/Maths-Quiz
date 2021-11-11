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
def question(): # TODO: Ask if the user wants to be timed
  start = time.time() #Starts the timer
  score = 0 # ! Define this
  print("Here come the questions, remember to press enter when you have typed your answer")
  time.sleep(2)
  for i in range(5): #Loops the question generator 10 times
    num1 = random.randint(n1,n2) #Generates a random number using the factors from the diff() function
    num2 = random.randint(n1,n2)
    
    answer = num1 * num2 #Defines the answer
    guess = ""
    guess_count = 0
    out_of_guesses = False
    question = f"\n{num1} x {num2}\n"

    print(question) #Prints the question

    while(guess != answer and not(out_of_guesses)):
      if(guess_count < guess_limit):
        guess = int(input("Please type the answer here (press enter afterwards): "))  
        guess_count += 1
      else:
        out_of_guesses = True

    if(out_of_guesses == True):
      print(f"\nOut of guesses, the answer was {answer}\n")
      stop = time.time() #Stops the timer
      break
    else:
      print("\nThe answer is correct!\n")
      score += 1

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
    guess_limit = 2
    question()

    prompt = input("Test again? (y/n): ")
    if(prompt.lower() != "y"):
      break