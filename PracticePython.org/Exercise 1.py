# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
# tells them the year that they will turn 100 years old.

count = 0

# Get user input
name = input("What is your name: ")
age = int(input("What is your age: "))
number = int(input("How many times you want the sentence to print: "))

# Calculate the year the user will turn 100
year = str((2020-age)+100)

# Prints it as many times as the user said
while count < number:
    print(name + " will turn 100 in " + year)
    count += 1