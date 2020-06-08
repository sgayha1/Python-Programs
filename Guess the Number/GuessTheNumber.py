# By Skylar Gayhart June 2, 2020

# Program randomly generates a number from a list then the user guesses until they are correct

import random  # To generate a random number


def pick_number():  # Will pick a number from a list (1-20)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]  # List number chosen from

    index = random.randrange(len(numbers))  # Picks a number from the list randomly
    chosen_number = numbers[index]  # Picks the number from the list

    return chosen_number  # Returns the number chosen


def guess_number(number):  # User guesses the number

    num = str(number)  # Makes number a string stored in num so that it can be compared to the guess
    used = []  # Initializing an empty list for later when used letters need to be displayed
    wrong = True  # Makes "win" false until user win

    guess = input("Pick a number between 1 and 20: \n")  # Puts user input into guess

    # First try is correct
    if guess == num:
        print("Correct! The number was " + num)
        # Changes the bool to False so that the while loop does not run
        wrong = False

    # If first try is not correct
    else:
        while wrong:  # Runs until the correct answer is given

            used.append(guess)

            # Prints a list of numbers previously used
            print("Used numbers: ")
            print(used)
            print("\n")

            # Asks user for another guess
            print(str(guess) + " is not the number! Try again\n")
            guess = input("Guess a number between 1 and 20: ")

            if guess == num:  # Breaks out of loop when correct
                print("Correct! The number was " + num)
                break


print("\n===========================")
print("| Welcome to the Program! |")
print("===========================")

print("\nDirections: In this program, you will be given a random number in between 1 and 20 to guess.\n\n")

# Chooses a number
chosen = pick_number()

# Gets guesses until guess is correct
guess_number(chosen)

print("\n===============")
print("| Program Done |")
print("================")




