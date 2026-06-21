# Approach 1: Brute Force
# Time Complexity: O(n²)
# Space Complexity: O(1)

class Solution:
    def twoSum(self , nums , target):
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
                

# Approach 2: HashMap
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def twoSum(self, nums , target):
        hashmap = {}
        for i , num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return[hashmap[complement] , i]
            hashmap[num] = i
            