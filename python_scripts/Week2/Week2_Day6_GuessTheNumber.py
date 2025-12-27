# Day6_GuessTheNumber
# Task: Set a secret number in the code.
# Repeatedly ask the user to guess the number.
# Print:
#   "Too high", "Too low", or "Correct".
# Use a while loop to continue until correct.
import random 
secret_code= random.randint(1,100) 
guess=int(input("what is your guess?"))
while guess != secret_code:
    if guess > secret_code:
        print("too high")
    elif guess < secret_code:
        print("too low")
    next_guess=int(input("what is your next input?"))
    guess=next_guess
if guess ==secret_code:
    print("correct")