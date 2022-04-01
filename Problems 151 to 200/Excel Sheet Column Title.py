# https://leetcode.com/problems/excel-sheet-column-title

# Runtime: 40 ms, faster than 58.31% of Python3 online submissions for Excel Sheet Column Title.
# Above average runtime, there may be more efficient implementations without using a while loop.

# Memory Usage: 13.8 MB, less than 96.53% of Python3 online submissions for Excel Sheet Column Title.
# Excellent memory usage, the letter variable is technically unnecessary but left in for readability.


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # adapted from: https://youtu.be/42jn_cl7g00
        
        res = ""
        
        while columnNumber > 0:
            columnNumber -= 1
            
            letter = chr((columnNumber % 26) + 65)
            res = letter + res
            
            columnNumber //= 26
            
            
        return res
