'''

  diff.py

  Author: Daniel Lagesse
  Date: 2021-10-20
  Version: 1

  Difficulty Component

'''
#-------Functions-------
def diff():
  global n1, n2, guess_limit
  while(True):
    difficulty = input(str("Please enter your desired difficulty (easy/medium/hard): "))
    if(difficulty == "easy"):
      n1 = 1
      n2 = 10
      guess_limit = 3
      print(f"n1 = {n1}, n2 = {n2}, guess_limit = {guess_limit}")
      break
    elif(difficulty == "medium"):
      n1 = 2
      n2 = 12
      guess_limit = 2
      print(f"n1 = {n1}, n2 = {n2}, guess_limit = {guess_limit}")
      break
    elif(difficulty == "hard"):
      n1 = 2
      n2 = 20
      guess_limit = 1
      print(f"n1 = {n1}, n2 = {n2}, guess_limit = {guess_limit}")
      break
    else:
      print("\nPlease enter a valid difficulty\n")
      continue
  return

#-------Main Routine--------
if(__name__ == "__main__"):
  while(True):
    diff()

    prompt = input("Test again? (y/n): ")
    if(prompt.lower() != "y"):
      break