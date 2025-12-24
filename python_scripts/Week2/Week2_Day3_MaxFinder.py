# Day3_MaxFinder
# Task: Ask the user to input 5 numbers, one by one.
# Use a loop and comparisons to find the largest number.
# Do NOT use lists or the built-in max() function.
# Print the maximum at the end.

### n refers to n rounds or n numbers that users want to put in .
def max_input(n):
    user_input=int(input("what number would u like to put in first:"))
    i=1
    while i< n:
        user_Nextinput=int(input(f"Enter number {i+1}:"))
        if user_Nextinput >=user_input:
            user_input=user_Nextinput
        i += 1
    print(f"The maxium is: {user_input}")

max_input(5)


