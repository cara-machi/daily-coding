# Day3_ListSearchAndIndex
# Task: Ask the user to enter numbers separated by spaces.
# Then ask for a target number.
# Print:
#   - whether the target exists in the list,
#   - all indices where it appears.
# Do NOT use list.index().
# Use a loop.

# Day3_ListSearchAndIndex

# 1. Get user input and convert to list of integers
user_input = input("Enter numbers separated by spaces: ")
parts = user_input.split()  # Split into string list

numbers = []
for part in parts:
    numbers.append(int(part))  # Convert each to integer

# 2. Get target number
target = int(input("Enter target number to search: "))

# 3. Search for target and record indices
indices = []  # Store all positions where target appears
for i in range(len(numbers)):  # Loop through indices (0, 1, 2, ...)
    if numbers[i] == target:
        indices.append(i)  # Record this index

# 4. Print results
if indices:  # If indices list is not empty
    print(f"Target {target} exists in the list.")
    print(f"It appears at indices: {indices}")
else:
    print(f"Target {target} does not exist in the list.")