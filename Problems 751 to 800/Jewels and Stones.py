# https://leetcode.com/problems/jewels-and-stones

# Runtime: 23 ms, faster than 99.27% of Python3 online submissions for Jewels and Stones.
# Excellent runtime, I thought this approach would be inefficient but it's consistently quick.

# Memory Usage: 13.8 MB, less than 63.32% of Python3 online submissions for Jewels and Stones.
# Decent memory usage, counting each individual occurence may be taking up too much memory.


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        count = 0
        
        for j in jewels:
            count += stones.count(j)
            
            
        return count
