# Day4_RecursiveSum
# Task: Write a recursive function recursive_sum(n)
# that returns the sum of numbers from 1 to n.
# Do NOT use loops.
# Define a clear base case and recursive case.

def recursive_sum(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n+recursive_sum(n-1)

