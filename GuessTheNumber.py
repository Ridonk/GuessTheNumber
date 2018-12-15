#!/bin/python

# Guess The Number uses the random module to generate a number.
# The user then puts in a guess as to what that number is and the program indicates either more or less.

import random


def is_num(x):
    try:
        return int(x)
    except ValueError:
        return False


def compare_number(val, comp):
    if comp < val:
        return -1
    elif comp > val:
        return 1
    else:
        return 0


def check_input(argx):
    if argx is not int:
        return -1
    else:
        return 1


def get_lower():
    num = False
    while num is False:
        lower_bound = is_num(input("Choose a minimum number: "))
        if lower_bound is not False:
            print("Lower bound saved. " + str(lower_bound))
            return int(lower_bound)


def get_upper():
    num = False
    while num:
        upper_bound = is_num(input("Choose a maximum number: "))
    print("Upper bound saved. " + str(upper_bound))
    return int(upper_bound) # Convert to lower and test


def get_guess(lower, upper):
    get_value = True
    while get_value:
        user_guess = input("Please guess a number between " + str(lower) + " and " + str(upper) + ":")
        if check_input(user_guess) == 1:
            return user_guess
        else:
            print("Invalid input... Try again with an integer number.")


def main():
    lower = get_lower()
    upper = get_upper()
    rand = random.randint(lower, upper)
    user_correct = False
    while user_correct is not True:
        guess = get_guess(lower, upper)
        compare = compare_number(rand, guess)
        if compare == -1:
            print("Too low... Try again!")
        elif compare == 1:
            print("Too high... Try again!")
        else:
            print("Good job! You guessed the number!")
            user_correct = True
    quit(0)


while True:
    main()
