# https://leetcode.com/problems/max-number-of-k-sum-pairs

# Runtime: 712 ms, faster than 80.13% of Python3 online submissions for Max Number of K-Sum Pairs.
# Good runtime, using the seen set may be adding O(1) operations unnecessarily, could take out and replace.

# Memory Usage: 27 MB, less than 54.91% of Python3 online submissions for Max Number of K-Sum Pairs.
# Okay memory usage, having the seen set is likely squeezing a bit more memory than is really needed.


from collections import Counter


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # thanks to: https://youtu.be/SP-YdgObPAQ
        
        c = Counter(nums)
        seen = set()
        res = 0
        
        for n in c:
            if n not in seen and (k-n) in c:
                if n == k-n:
                    res += (c[n] // 2)
                
                else:
                    res += min(c[n], c[k-n])
                    
                seen.add(n)
                seen.add(k-n)
                
                
        return res
