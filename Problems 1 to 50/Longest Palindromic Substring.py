# https://leetcode.com/problems/longest-palindromic-substring

# Runtime: 1519 ms, faster than 42.83% of Python3 online submissions for Longest Palindromic Substring.
# Slow runtime for a program in general, but pretty fast compared to the others, since it's O(N^2) total

# Memory Usage: 14.4 MB, less than 35.11% of Python3 online submissions for Longest Palindromic Substring.
# Not sure how memory usage could be improved, those intermediate variables seem necessary


class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        result = ""
        resultLen = 0
        
        for i in range(len(s)):
            
            # odd length palindromes
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resultLen:
                    result = s[l:r+1]
                    resultLen = r - l + 1
                l -= 1
                r += 1
            
            
            # even length palindromes
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resultLen:
                    result = s[l:r+1]
                    resultLen = r - l + 1
                l -= 1
                r += 1
                
                
        return result
