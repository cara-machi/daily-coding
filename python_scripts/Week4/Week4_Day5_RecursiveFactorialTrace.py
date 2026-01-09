# Day2_RecursiveFactorialTrace
# Task: Write a recursive factorial function.
# Add print statements to trace:
#   - when the function is called
#   - when it returns
# Example output should show the call stack unfolding.
# Goal: understand execution order, not just correctness.

def factorial(n):
    print(f"→ factorial({n}) called")  
    
    if n == 0:
        print(f"  ← factorial({n}) returns 1")  
        return 1
    elif n == 1:
        print(f"  ← factorial({n}) returns 1")
        return 1
    else:
        print(f"  computing {n} * factorial({n-1})")
        result = n * factorial(n-1)  
        print(f"  ← factorial({n}) returns {result}")
        return result