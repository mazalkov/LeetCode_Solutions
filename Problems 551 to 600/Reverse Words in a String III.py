# https://leetcode.com/problems/reverse-words-in-a-string-iii/

# Runtime: 36 ms, faster than 89.32% of Python3 online submissions for Reverse Words in a String III.
# Excellent runtime, doing a join and list comprehension together seemed slow, but works well for this case.

# Memory Usage: 14.6 MB, less than 90.04% of Python3 online submissions for Reverse Words in a String III.
# Excellent memory usage as well, the list comprehension may be 'bloating' unnecessarily, but still performs.


class Solution:
    def reverseWords(self, s: str) -> str:
        
        
        return ' '.join([word[::-1] for word in s.split(' ')])
