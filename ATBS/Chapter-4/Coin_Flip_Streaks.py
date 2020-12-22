import random

coinFlip = []
numberOfStreaks = 0
count = 0
STREAK = 6  # Creates a constant for streak variable

for experimentNumber in range(10000):
    # Generates the list of heads and tails using 0 and 1
    for i in range(100):
        coinFlip.append(random.randint(0, 1))

    # Checks if there is a streak
    for i in range(len(coinFlip)):
        while i != 0:
            if coinFlip[i] == coinFlip[i-1]:
                count += 1
            else:
                count = 0

            if count == STREAK:  # A streak was found
                numberOfStreaks += 1

    coinFlip = []  # Resets the list

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
