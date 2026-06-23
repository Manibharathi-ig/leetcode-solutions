# Approach 1: Brute Force
# Time Complexity: O(n²)
# Space Complexity: O(n)



class Solution:
    def isAnagram(self, t, s):
        if len(s) != len(t):
            return False
        t = list(t)
        for char in s:
            if char in t:
                t.remove(char)
            else:
                return False
        return True
    

# Approach 2: Sorting
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class solution:
    def isAnagram(Self , s , t):
        return sorted(s) == sorted(t)
    

# Approach 3: HashMap (Optimized)
# Time Complexity: O(n)
# Space Complexity: O(n)
class solution:
    def isAnagram(self , s , t):
        if len(s) != len(t):
            return False
        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i] , 0)
        return countS == countT