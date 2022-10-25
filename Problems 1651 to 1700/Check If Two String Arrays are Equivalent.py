# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent

# Runtime: 32 ms, faster than 95.77% of Python3 online submissions for Check If Two String Arrays are Equivalent.
# Nearly perfect runtime, I thought a more 'manual' algorithm could be faster, but it seems built-ins are good here.

# Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Check If Two String Arrays are Equivalent.
# Perfect memory usage, assuming Python handles all memory for objects in a better way than could be done 'manually'.


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
