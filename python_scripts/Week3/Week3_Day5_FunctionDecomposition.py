# Day5_FunctionDecomposition
# Task: Write a program that:
#   - reads numbers from user input,
#   - uses separate functions to:
#       * parse input into a list,
#       * compute sum,
#       * compute average,
#       * compute max.
# The main program should only call these functions
# and print results.
# Goal: decompose logic into reusable functions.

# Parse input using function
numbers = parse_input(user_input)

if len(numbers) == 0:
    print("No numbers entered.")
    return

# Compute results using functions
total = compute_sum(numbers)
average = compute_average(numbers)
maximum = compute_max(numbers)

# Print results
print(f"Numbers: {numbers}")
print(f"Sum: {total}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")