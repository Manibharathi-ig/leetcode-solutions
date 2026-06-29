# 49. Group Anagrams
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.


# Approach 1: Brute force method
# Time complexity:0(n² * k log k)
# Space complexity:0(n)

class Solution:
    def groupAnagrams(self , strs):
        result = []
        visited = [False] * len(strs)

        for i in range(len(strs)):
            if visited[i]:
                continue
            group = strs[i]
            visited[i] = True

            for j in range(i+1, len(strs)):
                if not visited[j]:
                    if sorted(strs[i] == sorted(strs[j])):
                        group.append(strs[j])
                        visited[j] =True

            result.append(group)
        return result


# Approach 2: Hashmap(optimized)
# Time complexity: 0(n * k log k)
# Space complexity: 0(n * k)

class Solution:
    def groupAnagrams(self , strs):
        groups = {}
        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []
            groups[key].append(word)
        return list(groups.values())