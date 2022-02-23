# https://leetcode.com/problems/perfect-number

# Runtime: 32 ms, faster than 95.88% of Python3 online submissions for Perfect Number.
# Excellent runtime, only checking up to the square root, there could be better maths tricks.

# Memory Usage: 13.9 MB, less than 84.35% of Python3 online submissions for Perfect Number.
# Excellent memory usage, everything is clearly defined that has to be there, nothing else used.


# adapted from: https://donic0211.medium.com/leetcode-507-perfect-number-849365da3f9c
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        
        if num <= 1:
            return False
    
        div_sum = 1
        root = int(num**0.5)
        
        for i in range(2, root+1):
            if num % i == 0:
                div_sum += i + num/i
                
                
        return div_sum == num
