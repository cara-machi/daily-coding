# Week 1: Python Basics

## Day 1: Two Sum 

**Problem**
Given an array of integers `nums` and a target, return indices of the two numbers that add up to the target.
**Key Concepts**
- Array traversal using `for` loops
- Index selection using `if` conditions
- Return first valid pair

**Python Script** `Day1_TwoSum.py`

**Test Cases**
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
```python
maxProfit([7,1,5,3,6,4])  # Expected: 5
maxProfit([7,6,4,3,1])    # Expected: 0
maxProfit([1,2,3,4,5])    # Expected: 4
```

## Day 2: Maximum Ascending Subarray Sum

**Problem**
Given an array nums, return the maximum sum of any continuous subarray whose elements are strictly increasing

**Key Concepts**
- Single Pass Traversal with state maintentance
- Track running sum for current increasing sequence
- Reset sum when when ascending order breaks
- Compare local and global maximum 

**Python Script** `Day2_MaxAscendingSubarraySum.py`

**Test Cases**
```python
maxAscendingSum([10, 20, 30, 5, 10, 50])  # Expected: 65
maxAscendingSum([7, 6, 5, 4, 3])          # Expected: 7
maxAscendingSum([100])                    # Expected: 100
maxAscendingSum([])                       # Expected: 0
maxAscendingSum([1, 2, 3, 4, 5])          # Expected: 15
maxAscendingSum([3, 2, 1, 2, 3])          # Expected: 5
```