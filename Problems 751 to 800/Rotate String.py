# https://leetcode.com/problems/rotate-string

# Runtime: 28 ms, faster than 94.08% of Python3 online submissions for Rotate String.
# Brilliant runtime, I thought using a while loop would be slow but apparently not so much.

# Memory Usage: 13.8 MB, less than 75.15% of Python3 online submissions for Rotate String.
# Excellent memory usage, the result variable changing on each iteration doesn't seem to be a bad decision.


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if not s or not goal:
            return True
        
        res = ""
        
        i = 1
        
        while i < len(s):
            
            res = s[i:] + s[:i]
            
            if res == goal:
                return True
            
            i += 1
            
            
        return False
