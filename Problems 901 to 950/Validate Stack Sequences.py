# https://leetcode.com/problems/validate-stack-sequences

# Runtime: 108 ms, faster than 45.48% of Python3 online submissions for Validate Stack Sequences.
# Below average runtime, I think my while conditions are checking for unnecessary conditions.

# Memory Usage: 14.2 MB, less than 63.80% of Python3 online submissions for Validate Stack Sequences.
# Average memory usage, a stack and pointer must be stored so not sure how to improve this further.


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        # with help from: https://youtu.be/SeTsK_aNUWI
        stack = []
        ptr = 0
        
        for elem in pushed:
            stack.append(elem)
            
            while stack and ptr < len(popped) and stack[-1] == popped[ptr]:
                stack.pop()
                ptr += 1
                
                
        return ptr == len(popped)
