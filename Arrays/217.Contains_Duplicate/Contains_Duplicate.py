# Given an integer array nums, return true if any value appears 
# at least twice in the array, and return false if 
# every element is distinct.


# Example 1:

# Input: nums = [1,2,3,1]

# Output: true

# Explanation:

# The element 1 occurs at the indices 0 and 3.
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
                return True
            seen.add(num)
        return False
    


