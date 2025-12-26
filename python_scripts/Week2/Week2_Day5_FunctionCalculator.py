# Day5_FunctionCalculator
# Task: Define four functions:
#   add(a, b), sub(a, b), mul(a, b), div(a, b).
# Reuse the menu logic from Day 4.
# Based on user choice, call the correct function
# and print the result.
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        return "zero is not dividable"
    return a/b
print("1: add(a,b) for sumaation of a&b")
print("2: sub(a,b) for subtraction btw a&b")
print("3:mul(a,b) for multiplication btw a&b")
print("4:div(a,b) for division btw a&b")

while True:
    choice=int(input("what function would u like to use, please coose the number1-4"))
    try:
        if 1<=choice<=4:
            break
        else:
            print("please choose 1-4")
    except ValueError:
        print("please choose number only")
a=int(input("what number do u opearte on fist"))
b=int(input("what number do u operate on second"))
if choice==1:
    result=add(a,b)
elif choice==2:
    result=sub(a,b)
elif choice==3:
    result=mul(a,b)
elif choice==4:
    result=div (a,b)
print (result)