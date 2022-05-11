# https://leetcode.com/problems/count-sorted-vowel-strings

# Runtime: 33 ms, faster than 80.43% of Python3 online submissions for Count Sorted Vowel Strings.
# Great runtime, taking a shortcut without using dynamic programming allows for direct calculation.

# Memory Usage: 13.8 MB, less than 96.44% of Python3 online submissions for Count Sorted Vowel Strings.
# Excellent memory usage, no need to define or use lists/dynamic arrays, just one single calculation.


from math import comb


class Solution:
    def countVowelStrings(self, n: int) -> int:
        # thanks to: https://github.com/kamyu104/LeetCode-Solutions/blob/master/C%2B%2B/count-sorted-vowel-strings.cpp
        
        return comb(n+4, 4)
