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