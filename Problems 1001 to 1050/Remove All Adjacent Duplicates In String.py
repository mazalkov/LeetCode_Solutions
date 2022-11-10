class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = [s[0]]
        
        for c in s[1:]:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
                
        return "".join(stack)
