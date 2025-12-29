# Day1_ListStatistics
# Task: Ask the user to enter numbers separated by spaces.
# Convert them into a list of integers.
# Compute and print:
#   - the sum,
#   - the average,
#   - the maximum,
#   - the minimum.
# Do NOT use built-in sum(), max(), or min().
# Use loops and accumulators.

user_input = input("Enter your numbers separated by spaces: ")
str_numbers = user_input.split()

numbers = []  
for i in str_numbers:
    numbers.append(int(i))

total = 0          
maximum = numbers[0]  
minimum = numbers[0]  

for num in numbers:
    total += num
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

average = total / len(numbers)  

print(f"Sum: {total}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")