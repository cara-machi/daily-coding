# Week 1: Python Basics

## Day 1: Two Sum 

**Problem**
Given an array of integers `nums` and a target, return indices of the two numbers that add up to the target.
**Key Concepts**
- Array traversal using `for` loops
- Index selection using `if` conditions
- Return first valid pair

**Python Script:** `Day1_TwoSum.py`

**Test Cases:**
```python
twoSum([3, 3], 6)           # Expected: [0, 1]
twoSum([2, 7, 11, 15], 9)   # Expected: [0, 1]
twoSum([1, 2, 3, 4], 5)     # Expected: [0, 3]
```

## Day 1: Best Time to Buy/Sell

**Problem**
Given an array prices, find the maximum profit by buying and selling once.

**Key Concepts**
- Traversal of array using for
- Track minimum price and maximum profit

**Python Script:** `Day1_BestTimeBuySell.py`

**Test Cases:**
maxProfit([7,1,5,3,6,4])  # Expected: 5
maxProfit([7,6,4,3,1])    # Expected: 0
maxProfit([1,2,3,4,5])    # Expected: 4
