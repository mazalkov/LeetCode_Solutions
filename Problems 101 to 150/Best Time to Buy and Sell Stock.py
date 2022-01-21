# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

# Runtime: 952 ms, faster than 91.92% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Good runtime, I think using enumerate and the else statement helps speed up the unnecessary cases.

# Memory Usage: 25 MB, less than 95.25% of Python3 online submissions for Best Time to Buy and Sell Stock.
# Very happy with memory usage, I thought having the index in enumerate would be too 'heavy' but it's fine.


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        minimum = prices[0]
        
        for i, price in enumerate(prices):
            
            if price < minimum:
                minimum = price
                
            else:
                profit = price - minimum if (price - minimum > profit) else profit
            
            
        return profit
