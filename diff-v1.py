'''
--------------------------------------------------------------------
  diff-v1.py

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
#This is the difficulty function which asks the user for factors. Their choice will determine the difficulty of the questions.
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

    confirm = input("\nAre you sure you want to play with these factors? (y/n): ")
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