# https://leetcode.com/problems/permutations-ii

# Runtime: 59 ms, faster than 91.77% of Python3 online submissions for Permutations II.
# Excellent runtime, although the time complexity is large, the algorithm works well.

# Memory Usage: 14.4 MB, less than 47.48% of Python3 online submissions for Permutations II.
# Below average usage, probably due to storing the current permutation in a changing list.


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # thanks to: https://youtu.be/qhBVWf0YafA
        
        res, cur = [], []
        counter = {n:0 for n in nums}
        for n in nums: counter[n] += 1
            
        def dfs():
            
            # base case
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for n in counter:
                # if we have a choice, append it and decrement
                if counter[n]:
                    cur.append(n)
                    counter[n] -= 1
                    
                    # do depth first search on new iteration
                    dfs()
                    
                    # add choice back to counter and pop from current
                    counter[n] += 1
                    cur.pop()
                    
                    
        dfs()
        return res
