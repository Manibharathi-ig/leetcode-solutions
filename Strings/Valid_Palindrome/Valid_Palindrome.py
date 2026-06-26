# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.


# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Approach 1: Reverese strings
# Time Complexity : O(n)
# space Complexity : O(n)

class solution:
    def isPalindrome(self , s):
        cleaned = 0
        for char in s:
            if char.isalnum():
                cleaned += char.lower()
        reverse = cleaned[::-1]
        return cleaned == reverse
    

# Approach 2: Two pointers (Optimized)
# Time Complexity : O(n)
# space Complexity : O(1)


class solution:
    def isPalindrome(self , s):
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left +=1
            while left < right and not s[right].isalnum():
                right -=1
            if s[left].low() != s[right].lower():
                return False
            left +=1
            right -=1
        return True