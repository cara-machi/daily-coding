# Day7_EvenOddFunctionDrill
# Task: Define a function is_even(n) that returns True or False.
# Ask the user for a number k.
# Use a loop to print numbers from 1 to k,
# and for each number print whether it is even or odd.
# Example: "2 even", "3 odd".

def is_Even(n):
    if n%2==0:
        return True
    else:
        return False
    

k=int(input("number:"))
i=1
while i <=k:
    print (i)
    if is_Even(i)==True:
        print(f"{i} even")
    else:
        print(f"{i} odd")
    i += 1
