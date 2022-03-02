# https://leetcode.com/problems/is-subsequence

# Runtime: 53 ms, faster than 37.05% of Python3 online submissions for Is Subsequence.
# Alright runtime, having the while loop with two conditions being "AND'd" may be slow.

# Memory Usage: 13.8 MB, less than 92.79% of Python3 online submissions for Is Subsequence.
# Very good memory usage, only need to define two pointer variables and compare them to lengths.


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i, j = 0, 0
        
        while i < len(s) and j < len(t):
            
            if s[i] == t[j]:
                i += 1

            j += 1
            
            
        return i == len(s)
