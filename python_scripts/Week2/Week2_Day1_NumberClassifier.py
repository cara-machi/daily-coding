# Week2-Day1_NumberClassifier
# Task: Ask the user for an integer and classify it as:
#   - positive, negative, or zero
#   - and also even or odd.
# Use if / elif / else and the modulo operator.
# Print clear messages for each case.

user_input=input("Enter an integer to classify:")
number = int(user_input)
def NumberClassifier(number):
    if number ==0:
        print (f"{number} is zero")
    elif number >0:
        print (f"{number} is positive")
        if number %2==0:
            print (f"{number} is even") 
        else:   
            print (f"{number} is odd")
    else:
        print(f"{number} is negative")
        if number %2==0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")
NumberClassifier(number)