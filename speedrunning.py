"""
--------------------------------------------------------------------
  speedrunning.py

   Project: Multiplication Maths Quiz
    Author: Daniel Lagesse
      Date: 2021-11-22
   Version: 1
    Python: 3.9.4

  Speedrunning Version
--------------------------------------------------------------------
  This program is a maths quiz designed for anyone above the age of 9.
  The user will face 10 randomly generated multiplication maths questions, these will be controlled by a difficulty system.
  The user has a choice of three difficulties: easy, medium or hard.
  Easy will only generate 1 to 10 times tables.
  Medium will generate from 2 to 12 times tables.
  Hard will generate from 2 to 20 times tables.
  The user will gain a point for correctly answering a question and a point will be revoked for every incorrectly answered question.
  The user will also be timed.

  The program is structured with components which all function together to run the quiz.
  Functions include: intro(Introduces the user), diff(Allows the user to select the difficulty), questions(Generates the questions),
  guess_validator(Ensures the user doesn't input an incorrect value), and answer_checker(Checks if the user's answer is correct).
--------------------------------------------------------------------
"""
# -------Libraries-------
# Imports the random library which allows the program to generate random
# numbers for the question
from random import randint
# Imports the time library which allows the program to slow down the interval
# between actions and allows the quiz to be timed
from time import perf_counter
import sys

# -------Functions-------

# This is the difficulty function which asks the user for their desired
# difficulty. Their choice will determine the difficulty of the questions.


def diff():
    while True:  # Loops incase the user enters an invalid difficulty
        difficulties = {
            "easy": (1, 10),
            "medium": (2, 12),
            "hard": (2, 20),
            "legendary": (20, 100),
        }
        difficulty = input(
            "\nPlease enter the desired difficulty (easy/medium/hard/legendary): "
        ).lower()
        # Checks that the user input matches one of the difficulties. If not,
        # the user will be prompted to enter again
        if difficulty in difficulties:
            return difficulties[difficulty]
        print("Invalid difficulty entered, please try again")


# This is the answer checker, it checks if the user's guess is the same as the
# answer, if it is, the user gains a point, if not, a point is revoked (This
# function is designed to work within the question function)


def answer_checker(question, answer, score):
    keep_going = True
    while keep_going:  # Loops to ensure that an invalid value cannot be stored
        try:
            guess = int(input("Please type the answer here: "))
            keep_going = False
        except ValueError:
            print("Invalid value entered, please enter a number and try again")
            # Prints the question again so the user doesn't have to scroll up
            print(question)

    if guess == answer:
        score += 1  # Adds 1 point to the score
        print(f"The answer is correct! Your score is now {score}")
    else:
        print(f"Incorrect, the answer was {answer}. Your score is now {score}")
    return score


# This is the question generator, it will generate 10 random questions using
# the factors from the diff() function.


def questions(factor_one, factor_two):
    QUESTION_AMOUNT = 10  # Sets the amount of questions to generate
    score = 0  # Sets the score to 0 every time the program is activated.
    start = perf_counter(
    )  # Starts the timer and stores the recorded time in a variable
    for _ in range(QUESTION_AMOUNT):  # Loops the question generator 10 times
        # Generates a random number using the factors from the diff() function
        num1 = randint(factor_one, factor_two)
        num2 = randint(factor_one, factor_two)

        answer = num1 * num2  # Defines the answer for each question
        # Sets the question using the randomly generated numbers
        question = f"\n{num1} x {num2}\n"

        print(question)  # Prints the question

        score = answer_checker(question, answer,
                               score)  # Calls the answer_checker function

    # Subtracting the start time from stop time allows us to find the user's
    # time.
    user_time = perf_counter() - start

    # {user_time:.2f} Displays the user's time to 2 significant figures
    print(f"You got {score}/10 questions right in a time of {user_time:.2f}s")


# -------Main Routine-------

if __name__ == "__main__":
    while True:  # Loops the entire quiz if the user wishes to play again
        factor_one, factor_two = diff()  # Calls the diff function
        questions(factor_one, factor_two)  # Calls the questions function

        # Asks if the user wants to play again and stores their choice in a
        # variable
        play_again = input("Play again? (y/n): ")
        if not play_again.lower().startswith("y"):
            print("Thanks for playing, goodbye!\n")
            sys.exit()
