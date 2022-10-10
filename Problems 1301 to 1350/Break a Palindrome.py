# https://leetcode.com/problems/break-a-palindrome

# Runtime: 47 ms, faster than 65.00% of Python3 online submissions for Break a Palindrome.
# Average runtime, this algorithm could probably be made faster by moving the checks around

# Memory Usage: 14 MB, less than 13.13% of Python3 online submissions for Break a Palindrome.
# Poor memory usage, likely due to the for loop taking a lot of variables and using them elsewhere


class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
    # thanks to: https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/break-a-palindrome.py
        
        if len(palindrome) == 1:
            return ""
        
        for i in range(len(palindrome)//2):
            if palindrome[i] != 'a':
                return palindrome[:i] + 'a' + palindrome[i+1:]
            
            
        return palindrome[:-1] + 'b'
