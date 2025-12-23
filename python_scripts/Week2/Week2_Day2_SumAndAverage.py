# Day2_SumAndAverage
# Task: Ask the user how many numbers they will enter (n).
# Then use a loop to read n numbers one by one.
# Compute and print:
#   - the total sum
#   - the average.
# Use an accumulator variable and a loop.

user_input=input("how many numbers would like to put:")
n =int(user_input)
total_sum=0
for i in range(1,n+1):
    number=int(input("What the number you want to put in this cycle:"))
    total_sum += number
avg=total_sum/n
print(f"{total_sum} is the total sum of the numbers")
print(f"{avg} is the average of the group of these numbers")

