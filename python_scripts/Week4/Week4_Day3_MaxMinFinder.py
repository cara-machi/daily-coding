# Day3_MaxMinFinder
# Task: Ask the user to input 5 numbers, one by one.
# Determine and print the maximum and minimum numbers.
# Do NOT use max() or min().
# Use loops and comparisons.

def main():
    number=[]
    for i in range (5):
        num=int(input(f"what is your {i+1} number:"))
        number.append(num)

    maxnum=number[0]
    minnum=number[0]
    for i in range(5):
        if number[i]>maxnum:
            maxnum=number[i]
        if number[i]<minnum:
            minnum=number[i]
    
main()


