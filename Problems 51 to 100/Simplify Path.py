# https://leetcode.com/problems/simplify-path

# Runtime: 32 ms, faster than 92.29% of Python3 online submissions for Simplify Path.
# Excellent runtime, the if-else condition structure seems to be optimised for the task.

# Memory Usage: 14 MB, less than 57.22% of Python3 online submissions for Simplify Path.
# Above average memory usage, having both a stack and a buffer may be unnecessary for this.


class Solution:
    def simplifyPath(self, path: str) -> str:
        # solved with much help from: https://youtu.be/qYlHrAKJfyA
        
        stack = []
        buffer = ""
        
        for c in path + "/":
            if c == "/":
                if buffer == "..":
                    if stack: stack.pop()
                
                elif buffer and buffer != ".":
                    stack.append(buffer)
                
                buffer = ""
                
            else:
                buffer += c
                
            
        return "/" + "/".join(stack)
