# Week2Day1:
- Today I learned: **input/output interaction with users**
    User input starts as a string from input();
    Convert it with int() to math. 

# Week2Day2:
- Today I learned: 
1. Use range() for generating sequence of numbers, not tuples directly
```python 
# Wrong: only loops twice if n=5
for i in (1, n):      # loops: 1, 5
# Right: loops n times  
for i in range(1, n+1):  # loops: 1, 2, 3, 4, 5
```
2. return is only for functions; loop use print for output 
```python
# Outside function - use print
total = 0
for i in range(3):
    total += i
print(total)  # ✅ Correct

# Inside function - can use return  
def calculate():
    total = 0
    for i in range(3):
        total += i
    return total  # ✅ Correct
```
**Use range to loop n times, and save return for functions only."**

# Week2Day3
1. f-string functions the same way in input() as in print()
```python
user_input=int(input(f"Enter number{i+1}:"))
```
2. need to pay attention to the numbers of iterations, i could initiallized to be 1 or 0 

# Week2Day4
1. print menu line-by-line fopr clear user interation, not as a raw list. 
2. == compare values, = assign values 
3. handle edge cases like user typos or invalid input 
4. use a loop with break to re-prompt on error and exit on valid input. 
```python 
while True:
    try:
        choice = int(input("Enter choice(1-4):))
        if 1<=choice<=4:
            break
        else:
            print("Invalid! Please ente 1-4")
    except ValueError:
        print("Please enter a number!")

```
# Wee2Day5 
1. Zero-division handling: 
- check at either function definition or call site. 
- **Recommended encapsulate in function definition for clearer calls**
2. Variable scope:
- Functions create local scope; result must be defined in all branches
- espeically in edgey situations like zero-division
3. input validation pattern:
- while True: loop with try/excpet ValueError for robust user input. 
4. Conditional structure:
- Use if/elif/elif/elif chain:
- The last can be else depending on needs. 
5. Subtle difference btw return an print
- **Functions should return values; printing is for user interaction**
```python
def div(a,b):
    if b==0:
        print("zero is not dividable")  # 1. notice 
    return a/b                          # 2. but still run a/b when b=0

def div(a,b):
    if b==0:
        return "Error: Cannot divide by zero"  # key: direcly return 
    return a/b                                 # execute when b!=0
```
- Return could directly stop the division when b==0