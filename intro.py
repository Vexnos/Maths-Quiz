'''
--------------------------------------------------------------------
  intro.py

   Project: Multiplication Maths Quiz
  Standard: 91883 & 91884
    School: Mountainview Highschool
    Author: Daniel Lagesse
      Date: 2021-11-11
   Version: 1
    Python: 3.9.4

  Introduction Component
--------------------------------------------------------------------
'''
#-------Libraries-------
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
  Your final score and time will be presented at the end of the questions.
  Good luck, User!
  ''')

  time.sleep(5) #Tells the program to sleep for 5 seconds before continuing

  ready = input("Are you ready to continue? (y/n): ")
  if(ready.lower() != "y"):
    print("Okay, quitting the program")
    quit()

  return

#-------Main Routine-------
if(__name__ == "__main__"):
  while(True):
    intro()

    prompt = input("Test again? (y/n): ") # Test Code
    if(prompt.lower() != "y"):
      break