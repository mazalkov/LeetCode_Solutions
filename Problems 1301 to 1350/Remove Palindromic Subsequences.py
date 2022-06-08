# https://leetcode.com/problems/remove-palindromic-subsequences

# Runtime: 34 ms, faster than 73.76% of Python3 online submissions for Remove Palindromic Subsequences.
# Good runtime, the program structure seems optimal, most likely the palindrome check in the middle could be faster.

# Memory Usage: 13.8 MB, less than 53.87% of Python3 online submissions for Remove Palindromic Subsequences.
# Good memory usage, assuming that the only extra comes from storing a reverse string, this could be improved as above.


class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # thanks to: https://youtu.be/M8gA5JOopLw
        
        if not s:
            return 0
        
        elif s == s[::-1]:
            return 1
        
        else:
            return 2
