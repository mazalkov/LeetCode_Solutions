# https://leetcode.com/problems/first-unique-character-in-a-string

# Runtime: 84 ms, faster than 94.85% of Python3 online submissions for First Unique Character in a String.
# Very good runtime, creating a Counter should be fast, and indexing through it for values of 1 should be linear.

# Memory Usage: 14.2 MB, less than 85.28% of Python3 online submissions for First Unique Character in a String.
# Good memory usage, only the Counter is defined and some intermediate variables during for indexing and so on.


from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        c = Counter(s)
        
        for i in range(len(s)):
            if c[s[i]] == 1:
                return i
        
        # no uniques, return -1
        return -1
