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

