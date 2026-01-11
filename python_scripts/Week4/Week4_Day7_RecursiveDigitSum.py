# Day3_RecursiveDigitSum
# Task: Write a recursive function digit_sum(n)
# that returns the sum of digits of n.
# Example: digit_sum(1234) → 10
# Do NOT convert the number to a string.

def digit_sum(n):
    if n<10:
        return n
    else
        return n%10+digit_sum(n//10)
        