'''
--------------------------------------------------------------------
  speedrunning.py

   Project: Multiplication Maths Quiz
    Author: Daniel Lagesse
      Date: 2021-11-22
   Version: 1
    Python: 3.9.4

  Speedrunning Version
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

#This is the difficulty function which asks the user for their desired difficulty. Their choice will determine the difficulty of the questions.
def diff():
  global n1, n2 #Makes the factors for the randomly generated questions global so other functions can access them.
  while True: #Loops incase the user enters an invalid difficulty
    difficulties = ["easy", 
                    "medium", 
                    "hard",
                    "legendary"]
    difficulty = input("\nPlease enter the desired difficulty (easy/medium/hard/legendary): ")
    if difficulty.lower() in difficulties: #Checks that the user input matches one of the difficulties. If not, the user will be prompted to enter again
      if difficulty == "easy":
        n1 = 1 #Defines the first factor
        n2 = 10 #Defines the second factor
        break #Breaks the while loop
      elif difficulty == "medium":
        n1 = 2
        n2 = 12
        break
      elif difficulty == "hard":
        n1 = 2
        n2 = 20
        break
      else:
        n1 = 20
        n2 = 100
        break
    else:
      print("Invalid difficulty entered, please try again")
      continue #Continues the loop

#This is the guess validator, it ensures the user cannot enter an invalid value as their answer to the question (This function is designed to work within the questions function)
def guess_validator():
  global guess #Makes the user's guess global so other functions can use it
  while True: #Loops to ensure that an invalid value cannot be stored
    try:
      guess = int(input("Please type the answer here: "))
    except ValueError:
      print("Invalid value entered, please enter a number and try again")
      print(question) #Prints the question again so the user doesn't have to scroll up
      continue
    break

#This is the answer checker, it checks if the user's guess is the same as the answer, if it is, the user gains a point, if not, a point is revoked (This function is designed to work within the question function)
def answer_checker():
  global score
  guess_validator() #Calls the guess_validator function to ensure an invalid value is not treated as an incorrect answer

  if guess == answer:
    score += 1 #Adds 1 point to the score
    print(f"The answer is correct! Your score is now {score}")
  else:
    print(f"Incorrect, the answer was {answer}. Your score is now {score}")

#This is the question generator, it will generate 10 random questions using the factors from the diff() function.
def questions():
  global question, answer, guess, score
  QUESTION_AMOUNT = 10 #Sets the amount of questions to generate
  score = 0 #Sets the score to 0 every time the program is activated.
  start = time.time() #Starts the timer and stores the recorded time in a variable
  for i in range(QUESTION_AMOUNT): #Loops the question generator 10 times
    num1 = random.randint(n1,n2) #Generates a random number using the factors from the diff() function
    num2 = random.randint(n1,n2)
    
    answer = num1 * num2 #Defines the answer for each question
    guess = "" #Defines guess to nothing so the next guess for the next question doesn't conflict
    question = f"\n{num1} x {num2}\n" #Sets the question using the randomly generated numbers

    print(question) #Prints the question

    answer_checker() #Calls the answer_checker function

  stop = time.time() #Stops the timer and stores the recorded time in a variable
  user_time = stop-start #Subtracting the start time from stop time allows us to find the user's time.

  print(f"You got {score}/10 questions right in a time of {user_time:.2f}s") #{user_time:.2f} Displays the user's time to 2 significant figures

#-------Main Routine-------
if __name__ == "__main__":
  while True: #Loops the entire quiz if the user wishes to play again
    diff() #Calls the diff function
    questions() #Calls the questions function

    play_again = input("Play again? (y/n): ") #Asks if the user wants to play again and stores their choice in a variable
    if play_again.lower() != "y":
      print("Thanks for playing, goodbye!\n")
      quit()