'''
--------------------------------------------------------------------
  usability_version.py

   Project: Multiplication Maths Quiz
  Standard: 91883 & 91884
    School: Mountainview Highschool
    Author: Daniel Lagesse
      Date: 2021-11-11
   Version: 1
    Python: 3.9.4

  Usability Version
--------------------------------------------------------------------
  This program is a maths quiz designed for anyone above the age of 9.
  The user will face 10 randomly generated multiplication maths questions, these will be controlled by a difficulty system.
  The user has a choice of three difficulties: easy, medium or hard. 
  Easy will only generate 1 to 10 times tables.
  Medium will generate from 2 to 12 times tables.
  Hard will generate from 2 to 20 times tables.
  The user will gain a point for correctly answering a question and a point will be revoked for every incorrectly answered question.
  The user will also be timed.

  The program is structed with components which all function together to run the quiz.
  Functions include: intro(Introduces the user), diff(Allows the user to select the difficulty), questions(Generates the questions),
  guess_validator(Ensures the user doesn't input an incorrect value), and answer_checker(Checks if the user's answer is correct).
--------------------------------------------------------------------
'''
#-------Libraries-------
import random #Imports the random library which allows the program to generate random numbers for the question
import time #Imports the time library which allows the program to slow down the interval between actions and allows the quiz to be timed

#-------Functions-------

#This is the intro function, it prints the intro message introdrucing the user to the quiz and asks if the user wants to continue the quiz.
def intro():
  time.sleep(1) #Tells the program to sleep for 1 second before printing the intro message
  print('''
  Welcome, user to my maths quiz! A quiz to practise your multiplication skills!
  The quiz allows you to choose your desired difficulty for 10 randomly generated multiplication questions.
  If you correctly guess a question, you will gain a point.
  If you incorrectly guess the question, you will lose a point (points can't go below 0).
  You will be timed during this quiz.
  Your final score and time will be presented at the end of the questions.
  Good luck, User!
  ''')

  time.sleep(5) #Tells the program to sleep for 5 seconds before continuing

  ready = input("Are you ready to continue? (y/n): ")
  if(ready.lower() != "y"):
    print("Okay, quitting the program")
    quit()

  return

#This is the difficulty function which asks the user for their desired difficulty. Their choice will determine the difficulty of the questions.
def diff():
  global n1, n2 #Makes the factors for the randomly generated questions global so other functions can access them.
  while(True):
    try:
      factor1 = int(input("\nPlease enter the 1st factor: "))
      factor2 = int(input("\nPlease enter the 2nd factor: "))
    except ValueError:
      print("Invalid value, please try again")
      continue
    if(factor1 > 0 and factor1 <= 20):
      n1 = factor1
    if(factor2 > 10 and factor2 <= 20):
      n2 = factor2
    else:
      print("Your first factor cannot be 0 or above 20, your second cannot be below 10 or above 20, please try again")
      continue

    confirm = input("\nAre you sure you want to play this difficulty? (y/n): ")
    if(confirm.lower() == "y"):
      break
    else:
      continue

  return

#This is the guess validator, it ensures the user cannot enter an invalid value as their answer to the question (This function is designed to work within the questions function)
def guess_validator():
  global guess #Makes the user's guess global so other functions can use it
  while(True): #Loops to ensure that an invalid value cannot be stored
    try:
      guess = int(input("Please type the answer here: "))
    except ValueError:
      print("Invalid value entered, please try again")
      print(question) #Prints the question again so the user doesn't have to scroll up
      continue
    break

  return

#This is the answer checker, it checks if the user's guess is the same as the answer, if it is, the user gains a point, if not, a point is revoked (This function is designed to work within the question function)
def answer_checker():
  global score
  guess_validator() #Calls the guess_validator function to ensure an invalid value is not treated as an incorrect answer

  if(guess == answer):
    score += 1 #Adds 1 point to the score
    print(f"The answer is correct! Your score is now {score}")
  else:
    score -= 1 #Revokes a point from the score if score is above 0
    print(f"Incorrect, the answer was {answer}. Your score is now {score}")
  
  return

#This is the question generator, it will generate 10 random questions using the factors from the diff() function.
def questions():
  global question, answer, guess, score
  score = 0 #Sets the score to 0 every time the program is activated.
  print("\nHere come the questions")
  time.sleep(2)
  start = time.time() #Starts the timer and stores the recorded time in a variable
  for i in range(10): #Loops the question generator 10 times
    num1 = random.randint(n1,n2) #Generates a random number using the factors from the diff() function
    num2 = random.randint(n1,n2)
    
    answer = num1 * num2 #Defines the answer for each question
    guess = "" #Defines guess to nothing so the next guess for the next question doesn't conflict
    question = f"\n{num1} x {num2}\n" #Sets the question using the randomly generated numbers

    print(question) #Prints the question

    answer_checker() #Calls the answer_checker function

  stop = time.time() #Stops the timer and stores the recorded time in a variable
  user_time = stop-start #Subtracting the start time from stop time allows us to find the user's time.

  print(f"You got a score of {score}/10 in a time of {user_time:.2f}s") #{user_time:.2f} Displays the user's time to 2 significant figures

  return

#-------Main Routine-------
if(__name__ == "__main__"):
  while(True): #Loops the entire quiz if the user wishes to play again
    intro() #Calls the intro function
    diff() #Calls the diff function
    questions() #Calls the questions function

    prompt = input("Play again? (y/n): ") #Asks if the user wants to play again and stores their choice in a variable
    if prompt.lower() != "y":
      quit()