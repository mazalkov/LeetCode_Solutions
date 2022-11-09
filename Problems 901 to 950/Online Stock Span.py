# https://leetcode.com/problems/online-stock-span

# Runtime: 422 ms, faster than 95.61% of Python3 online submissions for Online Stock Span.
# NEar perfect runtime, this seems to be a fast implementation by using a pseudo-stack.

# Memory Usage: 19.5 MB, less than 70.93% of Python3 online submissions for Online Stock Span.
# Excellent memory usage, dynamically modifying a list may be slow, could use other structures instead.


class StockSpanner:

    def __init__(self):
        self.prices = []        

    def next(self, price: int) -> int:
        
        count = 1
        
        while self.prices and self.prices[-1][0] <= price:
            count += self.prices.pop()[1]
        
        self.prices.append([price, count])
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
