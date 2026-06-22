# # Leetcode 217 - Contains Duplicate

# Approach 1: Brute Force
# Time Complexity: 0(n²)
# Space Complexity: 0(n)

class solution:
    def containsDuplicate(self , nums):
        for i in range(len(nums)):
            for j in range (i+1 , len(nums)):
                if nums[i] == nums[j]:
                    return True
            return False

# Aproach 2: Hashset (Optimized)
# Time Complexity : 0(n)
# Space Complexity : 0(n)

class Solution:
    def containsDuplicate(self , nums):
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                seen.add(num)
        return False
    


