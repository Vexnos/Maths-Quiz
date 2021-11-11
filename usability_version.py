'''

  usability_version.py

  Author: Daniel Lagesse
  Date: 2021-11-11
  Version: 1

  Usability Version

'''
#-------Libraries-------
import random
import time

#-------Functions-------
def intro():
  time.sleep(1)
  print('''
  Welcome, user to my math quiz! A quiz to practise your multiplication skills!
  The quiz allows you to choose your factors (Your first factor cannot be 0 or above 20, your second cannot be below 10 or above 20) 
  for 10 randomly generated multiplication questions.
  If you incorrectly guess the question, you will lose a point.
  Your final score will be shown at the end of the questions.
  Good luck, User!
  ''')
  time.sleep(5)

  return

def diff():
  global n1, n2
  while(True):
    try:
      factor1 = int(input("\nPlease enter the 1st factor (Press enter): "))
      factor2 = int(input("\nPlease enter the 2nd factor (Press enter): "))
    except ValueError:
      print("Invalid value, please try again")
      continue
    if(factor1 > 0 and factor1 <= 20):
      n1 = factor1
    if(factor2 >= 10 and factor2 <= 20):
      n2 = factor2
    else:
      print("Your first factor cannot be 0 or above 20, your second cannot be below 10 or above 20, please try again")
      continue

    confirm = input("Are you sure about these factors? (y/n): ")
    if(confirm.lower() == "y"):
      break
    else:
      continue

  return

def guess_validator():
  global guess
  while(True):
    try:
      guess = int(input("Please type the answer here (press enter afterwards): "))
    except ValueError:
      insults = ["You idiot, enter a number",
                 "Are you mentally handicapped? Enter a number",
                 "Come on, you know maths, enter a number",
                 "Unbelievable, how do you not know how to enter a number?"]
      
      insult = random.choice(insults)
      print(f"\n{insult}\n")
      print(question)
      continue
    break

  return

def answer_checker():
  global score
  guess_validator()

  if(guess == answer):
    score += 1
    print(f"The answer is correct! Your score is now {score}")
  else:
    if score <= 0:
      score = 0 #Checks that the score cannot be negative
    else:
      score -= 1
    print(f"Incorrect, the answer was {answer}. Your score is now {score}")
  
  return

def question():
  global question, answer, guess, score
  score = 0
  print("Here come the questions, remember to press enter when you have typed your answer")
  time.sleep(2)
  start = time.time() #Starts the timer
  for i in range(10): #Loops the question generator 10 times
    num1 = random.randint(n1,n2) #Generates a random number using the factors from the diff() function
    num2 = random.randint(n1,n2)
    
    answer = num1 * num2 #Defines the answer
    guess = ""
    question = f"\n{num1} x {num2}\n"

    print(question) #Prints the question

    answer_checker()

  stop = time.time()
  user_time = stop-start

  print(f"You got a score of {score}/10 in a time of {user_time:.2f}s") #Displays the user's time to 2 significant figures

  return

#-------Main Routine-------
if(__name__ == "__main__"):
  while(True):
    intro()
    diff()
    question()

    prompt = input("Play again? (y/n): ")
    if prompt.lower() != "y":
      quit()