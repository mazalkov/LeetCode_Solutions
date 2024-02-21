class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        if left < right:
            return self.rangeBitwiseAnd(left >> 1, right >> 1) << 1
        else:    
            return left
