'''
  
  user_input.py

  Author: Daniel Lagesse
  Date: 2021-11-11
  Version: 1

  User Input Component

'''
#-------Libraries-------
import random

#-------Functions-------
def input_validator():
  global guess
  example_question = "\n2 x 3\n"
  while(True):
    try:
      guess = int(input("Please type the answer here (press enter afterwards): "))
    except ValueError:
      insults = ["You idiot, enter a number",
                  "Are you mentally handicapped? Enter a number",
                  "Come on, you know maths, enter a number",
                  "Unbelievable, how do you not know how to enter a number?"]
      
      insult = random.choice(insults)
      print(f"\n{insult}\n")
      print(example_question)
      continue
    print(f"guess = {guess}")
    break

#-------Main Routine-------
if(__name__ == "__main__"):
  while(True):
    input_validator()

    prompt = input("Test again? (y/n): ")
    if(prompt.lower() != "y"):
      break