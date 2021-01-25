# https://leetcode.com/problems/palindrome-number/

# Runtime: 64 ms, faster than 59.01% of Python3 online submissions for Palindrome Number.
# Time complexity is pretty good, there's probably a faster algorithm but I don't know it.

# Memory Usage: 14.1 MB, less than 93.17% of Python3 online submissions for Palindrome Number.
# Used the same algorithm from reverse integer, so once again space is fairly good (eg embedded).


class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        reverse = 0
        
        y = x
        
        while y > 0:
            last_digit = y % 10
            reverse = (reverse*10) + last_digit
            y = y // 10
            
        return x == reverse 
