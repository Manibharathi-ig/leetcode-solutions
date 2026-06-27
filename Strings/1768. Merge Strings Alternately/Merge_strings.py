# 1768. Merge Strings Alternately

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.


# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s


# Approach 1 : Two pointers
# Time complexity : 0(n+m)
# Space complexity : 0(n+m)

class solution:
    def mergeAternately(self , word1, word2):
        i = 0
        j = 0
        result = ""

        while i < len(word1) and j < len(word2):
            result += word1[i]
            result += word2[j]

            i+=1
            j+=1

        result += word1[i:]
        result += word2[j:]

        return result
