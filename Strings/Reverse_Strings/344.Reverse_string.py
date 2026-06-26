# Reverse String

# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


# Approach  1 :  Brute force
# Time complexity = o(n)
# space complexity = o(n)



class Solution:
    def reverseString(self , s):
        new = []
        for i in range(len(s)-1,-1,-1):
            new.append(s[i])
        for i in range(len(s)):
            s[i] = new[i]

# Approach  2 :  Two pointers with python swap approach
# Time complexity = o(n)
# space complexity = o(1)

class Solution:
    def reverseString(self, s):
        left = 0
        right = len(s)-1

        while left < right:
            s[left],s[right] = s[right], s[left]
            left +=1
            right -=1


# Approach  3 :  Two pointers with temp variable approach
# Time complexity = o(n)
# space complexity = o(1)


class Solution:
    def reverseString(self , s):
        left = 0
        right = len(s) - 1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp

            left +=1
            right -=1




