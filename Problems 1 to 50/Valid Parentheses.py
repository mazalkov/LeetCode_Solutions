class Solution:
    def isValid(self, s: str) -> bool:
        
        if s.count('(') != s.count(')') or s.count('{') != s.count('}') or s.count('[') != s.count(']'):
            return False
        
        left = ['(', '{', '[']
        right = [')', '}', ']']
        stack = []
        
        for char in s:
            if char in left:
                stack.append(char)
                
            elif char in right:
                if not stack or stack[-1] != left[right.index(char)]:
                    return False

                else:
                    stack.pop()
        
        
        return not stack
