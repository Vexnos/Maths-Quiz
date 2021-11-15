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
    while(True):
      difficulty = input("\nPlease enter the desired difficulty (easy/medium/hard): ")
      if(difficulty.lower()) == "easy":
        n1 = 1
        n2 = 10
        break
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
        continue

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
    print(f"{n1} and {n2}")

    prompt = input("Test again? (y/n): ")
    if(prompt.lower() != "y"):
      break