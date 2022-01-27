# https://leetcode.com/problems/valid-anagram

# Runtime: 36 ms, faster than 96.30% of Python3 online submissions for Valid Anagram.
# Very good runtime for Python, seems like Counter has been efficiently designed.

# Memory Usage: 14.4 MB, less than 81.64% of Python3 online submissions for Valid Anagram.
# Could do an in-place check of the strings, but Counter appears to not take up much space.


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_Counter = Counter(s)
        t_Counter = Counter(t)
        
        
        return t_Counter == s_Counter
