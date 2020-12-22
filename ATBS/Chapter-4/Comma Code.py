# Write a function that takes a list value as an argument and returns a string with all the items separated by a comma
# and a space, with and inserted before the last item. For example, passing the previous spam list to the function would
# return 'apples, bananas, tofu, and cats'. But your function should be able to work with any list value passed to it.
# Be sure to test the case where an empty list [] is passed to your function.


def comma_code(list_value):

    # Checks if there are any values in list_value; If not, prints "No values!"
    if len(list_value) == 0:
        print("No values!")

    # Iterates through the list_value list and when it is the last word, puts "and" in front
    for i in range(len(list_value)):
        if i == len(list_value) - 1:
            print("and", list_value[i], end=" ")
        else:
            print(list_value[i] + ",", end=" ")


# Creates a list called values, the word and answer variables
values = []
word = ""
answer = ' '

# Gets user input for what String they want in the list
while True:
    # Gets user input, appends it to the list, then continues (if prompted to)
    word = input("Input a word to put into the list (enter STOP to stop): ")

    # Input validation
    if word == "STOP":
        break

    values.append(word)

comma_code(values)
