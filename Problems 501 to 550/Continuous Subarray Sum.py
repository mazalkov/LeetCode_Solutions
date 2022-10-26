# https://leetcode.com/problems/continuous-subarray-sum

# Runtime: 1120 ms, faster than 84.58% of Python3 online submissions for Continuous Subarray Sum.
# Good runtime, while I don't understand the algorithm too well, NeetCode has done well here.
 
# Memory Usage: 33.2 MB, less than 73.31% of Python3 online submissions for Continuous Subarray Sum.
# Good memory usage, storing a dict isn't too intensive, only have a few variables storing otherwise.


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        remainders = {0: -1}
        total = 0
        
        for i, num in enumerate(nums):
            total += num
            rem = total % k
            
            if rem not in remainders:
                remainders[rem] = i
                
            elif i - remainders[rem] > 1:
                return True
            
            
        return False
