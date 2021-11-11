'''

  intro.py

  Author: Daniel Lagesse
  Date: 2021-11-11
  Version: 1

  Introduction Component

'''
#-------Libraries-------
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

#-------Main Routine-------
if(__name__ == "__main__"):
  while(True):
    intro()

    prompt = input("Test again? (y/n): ")
    if(prompt.lower() != "y"):
      break