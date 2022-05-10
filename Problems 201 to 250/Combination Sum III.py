# https://leetcode.com/problems/combination-sum-iii

# Runtime: 40 ms, faster than 62.90% of Python3 online submissions for Combination Sum III.
# Good runtime, recursive depth first search may be slower compared to alternative solutions.

# Memory Usage: 14 MB, less than 29.87% of Python3 online submissions for Combination Sum III.
# Poor memory usage, likely due to creating many recursive calls which are added to the stack.


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # thanks to: https://youtu.be/LoycI7Y-hww
        
        res = []
        
        
        def dfs(stack, num, cur_sum):
            
            # base
            if len(stack) == k:
                if cur_sum == n:
                    res.append(stack)
                    return
                
            for i in range(num,9+1):
                
                if cur_sum + i > n:
                    break
                    
                dfs(stack+[i], i+1, cur_sum+i)
                
                
        dfs([], 1, 0)
        
        return res
