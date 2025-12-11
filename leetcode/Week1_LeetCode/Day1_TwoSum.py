# Day1_TwoSum.py

# Problem: Two SUm
# Concept: Array traversal + using indices
# Key idea: check all paris of numbers, return their indices when sum equals target
# Traversal: Go through all elements of a data structure, one by one 

# type : ignore
 def twoSum(nums,target):
    for i in range(len(nums)):
      for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
          return [i,j]
        
if __name__=="__main__":
  print(twoSum([3,3],6))
  print(twoSum([2,7,11,15],9))
  print(twoSum([3,2,4],6))
  













