'''
--------------------------------------------------------------------
  diff.py

   Project: Multiplication Maths Quiz
  Standard: 91883 & 91884
    School: Mountainview Highschool
    Author: Daniel Lagesse
      Date: 2021-10-20
   Version: 1
    Python: 3.9.4

  Difficulty Component
--------------------------------------------------------------------
'''
#-------Functions-------
#This is the difficulty function which asks the user for their desired difficulty. Their choice will determine the difficulty of the questions.
def diff():
  global n1, n2 #Makes the factors for the randomly generated questions global so other functions can access them.
  while(True): #Loops incase the user decides to change difficulty
    while(True): #Loops incase the user enters an invalid difficulty (This has to be inside two while loops otherwise the confirmation will trigger even if the input is invalid).
      difficulty = input("\nPlease enter the desired difficulty (easy/medium/hard): ")
      if(difficulty.lower()) == "easy":
        n1 = 1 #Defines the first factor
        n2 = 10 #Defines the second factor
        break #Breaks the while loop
      elif(difficulty.lower()) == "medium":
        n1 = 2
        n2 = 12
        break
      elif(difficulty.lower()) == "hard":
        n1 = 2
        n2 = 20
        break
      else:
        print("Invalid difficulty entered, please try again")
        continue #Continues the loop

    confirm = input("\nAre you sure you want to play this difficulty? (y/n): ")
    if(confirm.lower() == "y"):
      break
    else:
      continue

  return

#-------Main Routine--------
if(__name__ == "__main__"):
  while(True):
    diff()
    print(f"{n1} and {n2}") #This is for testing and will not be in the actual quiz

    prompt = input("Test again? (y/n): ")
    if(prompt.lower() != "y"):
      break