class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:

        def is_arithmetic(subarray):
            if len(subarray) < 2:
                return True

            diff = subarray[1] - subarray[0]

            for i in range(1, len(subarray) - 1):
                if subarray[i + 1] - subarray[i] != diff:
                    return False

            return True
        
        LENGTH = len(l)
        res = [None] * LENGTH

        for i in range(LENGTH):
            subarr = nums[l[i] : r[i]+1]
            res[i] = is_arithmetic(sorted(subarr))

        return res
