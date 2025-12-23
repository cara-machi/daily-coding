# Python Function Arguments: Quick Guide
**Define with placeholders, call with actual values**

## Definition
- Formal Parameter: Placeholder in function definition
- Actual Argument: Real value passed during function call

## Correct Usage
### FUNCTION DEFINITION (template)
```python
def greet(name):          # 'name' = formal parameter (placeholder)
    return f"Hi, {name}"

```
### FUNCTION CALL (actual use)
```python
greet("Flower")          # "Flower" = actual argument (real value)
result = greet("Flower") # Save return value
```

## Common Mistakes &Fix
### WRONG (using placeholder outside definition)
```python
greet(name)  # ❌ NameError: 'name' is not defined
```
### CORRECT (pass actual value)
```python
greet("Flower")  # ✅
```