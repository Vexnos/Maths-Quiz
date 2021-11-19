'''
--------------------------------------------------------------------
  play_again.py

   Project: Multiplication Maths Quiz
  Standard: 91883 & 91884
    School: Mountainview Highschool
    Author: Daniel Lagesse
      Date: 2021-11-03
   Version: 1
    Python: 3.9.4

  Play again component
--------------------------------------------------------------------
'''
#-------Main Routine-------
if(__name__ == "__main__"):
  while(True):

    prompt = input("Play again? (y/n): ")
    if(prompt.lower() != "y"):
      break