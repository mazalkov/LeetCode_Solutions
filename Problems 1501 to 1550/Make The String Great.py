# https://leetcode.com/problems/make-the-string-great

# Runtime: 34 ms, faster than 97.35% of Python3 online submissions for Make The String Great.
# Near perfect runtime, implementing a stack with some lookups and a swapcase seems fast.

# Memory Usage: 13.8 MB, less than 97.60% of Python3 online submissions for Make The String Great.
# Near perfect memory usage, would only have to store the entire string at most, dynamic allocation bad though.


class Solution:
    def makeGood(self, s: str) -> str:
        
        stack = []
        
        for char in s: 
            if stack and stack[-1] == char.swapcase():
                stack.pop()                         
                
            else: 
                stack.append(char)
        
        
        return "".join(stack)
