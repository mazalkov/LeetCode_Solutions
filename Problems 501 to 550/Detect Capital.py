# https://leetcode.com/problems/detect-capital

# Runtime: 28 ms, faster than 94.46% of Python3 online submissions for Detect Capital.
# Brilliant runtime, using in-built methods with simple 'or' checks should be fastest.

# Memory Usage: 13.8 MB, less than 96.96% of Python3 online submissions for Detect Capital.
# Excellent memory usage, nothing unnecessary is defined or used, only the word itself.


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        # having the checks in this order seems to be fastest
        return word.islower() or word.isupper() or word.istitle()
