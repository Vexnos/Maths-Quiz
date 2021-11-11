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
  The quiz has varying difficulties, easy (1 to 10 times tables) with 3 wrong guesses allowed, 
  medium (1, 12 times tables) with 3 wrong guesses allowed,
  and hard (2, 20 times tables) with 1 wrong guess allowed.
  If you run out of guesses, you lose! Good luck, user!
  ''')
  time.sleep(12)

  return

#-------Main Routine-------
if(__name__ == "__main__"):
  while(True):
    intro()

    prompt = input("Test again? (y/n): ")
    if(prompt.lower() != "y"):
      break