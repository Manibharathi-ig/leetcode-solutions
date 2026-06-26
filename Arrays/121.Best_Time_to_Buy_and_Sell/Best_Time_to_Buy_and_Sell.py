# Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.



# LeetCode 121 - Best Time to Buy and Sell Stock

# Approach 1: Brute Force
# Time Complexity: 0(n²)
# Space Complexity: 0(1)


class Solution:
    def maxProfit(self, prices):
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i+1 , len(prices)):
                profit = prices[j] - prices[j]
                maxProfit = max(maxProfit , profit)
            return maxProfit
        
# Approach 2: Sliding Window (Optimized)
# Time Complexity: 0(n)
# Space Complexity: 0(1)

class Solution:
    def maxProfit(self , prices):
        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            minPrice = min(minPrice, price)
            profit = price - minPrice
            maxProfit = max(maxProfit , profit)
        return maxProfit

