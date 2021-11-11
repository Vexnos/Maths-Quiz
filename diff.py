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
      factor1 = int(input("\nPlease enter the 1st factor (Type the factor then press enter): "))
      factor2 = int(input("\nPlease enter the 2nd factor (Type the factor then press enter): "))
    except ValueError:
      print("Invalid value, please try again")
      continue
    if(factor1 > 0 and factor1 <= 20):
      n1 = factor1
    if(factor2 >= 10 and factor2 <= 20):
      n2 = factor2
    else:
      print("Your first factor cannot be 0 or above 20, your second cannot be below 10 or above 20, please try again")
      continue

    confirm = input("\nAre you sure about these factors? (y/n): ")
    if(confirm.lower() == "y"):
      break
    else:
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