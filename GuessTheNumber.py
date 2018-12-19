#!/bin/python

# Guess The Number uses the random module to generate a number.
# The user then puts in a guess as to what that number is and the program indicates either more or less.

import random


# Determines if a given value (x) is in fact an integer and if so returns it, otherwise returns False and
# notifies the user of the error.
def is_num(x):
    try:
        return int(x)
    except ValueError:
        print(str(x) + " is not an integer. Please try again.")
        return False


# Compares a given value against a comparison input and returns -1 if too low, 1 if too high, and 0 if just right.
def compare_number(val, comp):
    if comp < val:
        return -1
    elif comp > val:
        return 1
    else:
        return 0


# This function serves to receive and call verification on user input for upper and lower bounds of the game.
def get_bound():
    while True:
        bound = is_num(input("Choose a number: "))
        if bound is not False:
            print("Bound saved. " + str(bound))
            return int(bound)


# This function serves to get the users guessed value
def get_guess(lower, upper):
    while True:
        user_guess = is_num(input("Please guess a number between " + str(lower) + " and " + str(upper) + ": "))
        if user_guess is not False:
            return user_guess


def main():
    lower = get_bound()
    upper = get_bound()
    rand = random.randint(lower, upper)
    user_correct = False
    user_guess_count = 0
    while user_correct is not True:
        guess = get_guess(lower, upper)
        compare = compare_number(rand, guess)
        if compare == -1:
            print("Too low... Try again!")
            user_guess_count += 1
        elif compare == 1:
            print("Too high... Try again!")
            user_guess_count += 1
        else:
            print("Good job! You guessed the number!")
            user_guess_count += 1
            print("It took you " + str(user_guess_count) + " attempts to guess the correct number!")
            user_correct = True
    while True:
        user_quit = input("Continue? (y/n)")
        if user_quit == 'y':
            main()
        elif user_quit == 'n':
            quit()


main()
