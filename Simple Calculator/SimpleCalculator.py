# Created by Skylar Gayhart, June 1, 2020

# Simple calculator application that keeps track of all operations performed and prints a list after each calculation

equations_completed = {}  # Keeps all values (equations and solutions) in this


# Functions to do arithmetic
def addition(first, second):
    return first + second


def subtraction(first, second):
    return first - second


def multiplication(first, second):
    return first*second


def division(first, second):
    # Input validation
    while second == 0:
        second = input("Pick a different number. Cannot divide by 0")

    return round(first/second)


def modulo(first, second):
    return first % second


# Used to display all solutions and equations done
def display():

    print("Equation\t\t" + "Solution")
    print("-------------------------")

    for k, v in equations_completed.items():
        print(str(k) + str(v))


# Condition for while loop
cont = True

# Try/except makes sure it will run well
try:
    # Continues until the cont variable is changed to false
    while cont:
        num1 = int(input("Enter your first number: "))
        num2 = int(input("Enter your second number: "))

        # Display a menu so the user can choose
        print("\n(0) Addition")
        print("(1) Subtraction")
        print("(2) Multiplication")
        print("(3) Division")
        print("(4) Modulo/Remainder")
        num = input("Choose an operation by inputting the corresponding number: ")
        num = int(num)

        # Dictionary to choose function accordingly
        operation = {
            0: addition(num1, num2),
            1: subtraction(num1, num2),
            2: multiplication(num1, num2),
            3: division(num1, num2),
            4: modulo(num1, num2),
        }

        # Uses the input to get a number from the dictionary
        y = operation.get(num)

        # Assigns a operator
        if num == 0:
            num = " + "
        if num == 1:
            num = " - "
        if num == 2:
            num = " * "
        if num == 3:
            num = " / "
        if num == 4:
            num = " % "

        # Adds to the list
        equations_completed[str(num1) + num + str(num2) + "\t\t\t\t"] = y
        display()

        # To stop or continue the loop
        answer = input("\nWould you like to continue? ('N' for no; 'Y' for yes): ")
        answer = answer.upper()  # To make sure the n or y is capital

        if answer == 'N':
            cont = False # Will break the loop
            break  # To make sure it breaks

    print("\nThis is the final list of all your equations. Take a screenshot!\n\n")
    display()

    print("\n================================")
    print("Thank you for using the program!")
    print("================================")

except ValueError as e:
    print(e)
