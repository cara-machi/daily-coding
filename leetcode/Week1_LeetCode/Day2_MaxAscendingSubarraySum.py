#Day2_MaxAscendingSubarraySum.py

#Problem: Find the maximum sum of any continuous subarray whose elements are strictly increasing are 
#Concept: Use a single-pass traversal that maintains a running sum for the current increasing and resets when the older breaks
#Keyidea: Track a local ascending subarray sum while preserving the global maximum across all segments
#Takeaway: Single-Pass problem can efficiently solve subarray problems by maintaining global variable


class Solution:
    def maxAscendingSum(self, nums:List[int]) ->int:
        current_sum=nums[0]
        max_sum=nums[0]
        for i in range(1,len(nums)):
           if nums[i]>nums[i-1]:
               current_sum += nums[i]
            else:
               max_sum=max(max_sum, current_sum)
               current_sum=nums[i]
        return max(max_sum, current_sum)
    