# https://leetcode.com/problems/last-stone-weight

# Runtime: 28 ms, faster than 96.47% of Python3 online submissions for Last Stone Weight.
# Excellent runtime, the while loop could be optimised to not need to perform max() twice each iteration.

# Memory Usage: 14 MB, less than 17.07% of Python3 online submissions for Last Stone Weight.
# Poor memory usage, likely due to the constant definition, popping and appending of variables.


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        if len(stones) <= 1:
            return stones[0]
        
        while len(stones) > 1:
          
            y = max(stones)
            stones.remove(y)
            x = max(stones)
            stones.remove(x)
            
            if x != y:
                stones.append(y-x)
                
                
        return stones[0] if stones else 0
