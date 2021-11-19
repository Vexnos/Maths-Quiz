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
    print("\n---Quiz Here---") #This is test code and will not be used in the final version

    play_again = input("\nPlay again? (y/n): ")
    if(play_again.lower() != "y"):
      print("Thanks for playing, goodbye!\n")
      quit()