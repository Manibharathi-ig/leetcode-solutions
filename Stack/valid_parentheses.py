# # 20. Valid Parentheses

# # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# # An input string is valid if:

# # Open brackets must be closed by the same type of brackets.
# # Open brackets must be closed in the correct order.
# # Every close bracket has a corresponding open bracket of the same type.

# # Example 1:

# # Input: s = "()"

# # Output: true

# # Example 2:

# # Input: s = "()[]{}"

# # Output: true

# # Example 3:

# # Input: s = "(]"

# # Output: false


# Approach 1: Brute force
# Time complexity: o(n²)
# space complexity: o(n)

class Solution:
    def isValid(self , s):
        previous = ""

        while s != previous:
            previous = s

            s = s.replace("()", "")
            s = s.replace("[]", "")
            s = s.replace("{}", "")

        return s == ""
    

# Approach 2: optimzed
# Time complexity: o(n)
# space complexity: o(n)

class Solution:
    def isValid(self, s):
        stack =[]
        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for char in s:
            if char not in pairs:
                stack.append(char)
            else:
                if not stack:
                    return False
                
                top = stack.pop()
                if top != pairs[char]:
                    return False
        return not stack

