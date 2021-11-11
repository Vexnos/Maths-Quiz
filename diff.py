'''

  diff.py

  Author: Daniel Lagesse
  Date: 2021-10-20
  Version: 1

  Difficulty Component

'''
#-------Functions-------
def diff():
  global n1, n2
  while(True):
    try:
      factor1 = int(input("Please enter the 1st factor (Press enter): "))
      factor2 = int(input("Please enter the 2nd factor (Press enter): "))
    except ValueError:
      print("Invalid value, please try again")
      continue
    if(factor1 > 0 and factor1 <= 20):
      n1 = factor1
    if(factor2 > 0 and factor2 <= 20):
      n2 = factor2
      break
    else:
      print("Your factors cannot be 0 or above 20, please try again")
      continue
  return

#-------Main Routine--------
if(__name__ == "__main__"):
  while(True):
    diff()
    print(f"{n1} and {n2}")

    prompt = input("Test again? (y/n): ")
    if(prompt.lower() != "y"):
      break