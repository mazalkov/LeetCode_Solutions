# https://leetcode.com/problems/find-players-with-zero-or-one-losses

# Runtime: 2961 ms, faster than 74.94% of Python3 online submissions for Find Players With Zero or One Losses
# Good runtime, the Counter implementation should lend to speed, but the for loop does not.

# Memory Usage: 68.1 MB, less than 93.83% of Python3 online submissions for Find Players With Zero or One Losses.
# Excellent memory usage, again using the Counter is likely one of the most space efficient methods.


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        c = collections.Counter()
        
        for win, loss in matches:
            c[win] += 0
            c[loss] += 1
            
        res = [[], []]
            
        for key in c:
            if c[key] == 0 or c[key] == 1:
                res[c[key]].append(key)
                
        res[0].sort()
        res[1].sort()
        
        
        return res
    
