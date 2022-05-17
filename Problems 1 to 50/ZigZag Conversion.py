# https://leetcode.com/problems/zigzag-conversion

# Runtime: 65 ms, faster than 76.58% of Python3 online submissions for Zigzag Conversion.
# Good runtime, although there are two nested loops, runtime complexity should be O(N).

# Memory Usage: 14 MB, less than 75.77% of Python3 online submissions for Zigzag Conversion.
# Good memory usage, the inbetween variable doesn't have to be declared but is done so for readability.


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # thanks to: https://youtu.be/Q2Tw6gcVEwc
        
        if numRows == 1:
            return s
        
        res = ""
        
        for row in range(numRows):
            increment = 2*(numRows-1)
            
            for i in range(row, len(s), increment):
                res += s[i]
                
                inbetween = i + increment - (2*row)
                if (row > 0) and (row < numRows-1) and (inbetween < len(s)):
                    res += s[inbetween]                    
                    
                    
        return res
