import random
import math

# Take input from user for lower and upper bounds
lower = int(input("Enter the lower bound:- "))

upper = int(input("Enter the higher bound:- "))

# generate a random number between 
# lower and higher
x = random.randint(lower, upper)

guess_chances = math.log(upper - lower + 1, 2)

print("\n\tYou've only ",
      round(guess_chances),
      " chances to guess the integer!\n")

# Initializing the number of guesses
count = 0

while count < guess_chances:
    count += 1

    # take guessing number as input
    guess = int(input("Guess the number:- "))

    # Condition test
    if x == guess:
        print("Congratulations, you guessed the number in ", count, " tries")
        break # break the loop if user guesses the number
    elif x > guess: 
        print("You guessed too low!")
    elif x < guess:
        print("You guessed to high!")

# if the user guesses more than the required guesses,
# let the user know
if count >= guess_chances:
    print("\nThe number is %d" % x)
    print("\tBetter luck next time!")