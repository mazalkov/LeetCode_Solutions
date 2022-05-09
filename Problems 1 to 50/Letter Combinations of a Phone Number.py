# https://leetcode.com/problems/letter-combinations-of-a-phone-number

# Runtime: 41 ms, faster than 54.70% of Python3 online submissions for Letter Combinations of a Phone Number.
# Average runtime, this recursive backtrack method brute forces all combinations, which may likely be improved upon.

# Memory Usage: 13.8 MB, less than 79.68% of Python3 online submissions for Letter Combinations of a Phone Number.
# Good memory usage, only storing the result and lookup table, which are both seemingly necessary due to the problem.


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        res = []
        
        lookup = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        
        def backtrack(i, currentStr):
            if len(currentStr) == len(digits):
                res.append(currentStr)
                return
            
            for c in lookup[digits[i]]:
                backtrack(i+1, currentStr + c)
                
        
        if digits:
            backtrack(0, "")
            
        return res
