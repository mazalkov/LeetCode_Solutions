# https://leetcode.com/problems/reverse-string

# Runtime: 208 ms, faster than 67.54% of Python3 online submissions for Reverse String.
# Good runtime, a while loop should be sufficient as this algorithm should be optimal.

# Memory Usage: 18.4 MB, less than 93.92% of Python3 online submissions for Reverse String.
# Very good memory usage, only storing a temporary variable which is necessary for 'switching'.


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        left, right = 0, len(s)-1
        
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            
            left += 1
            right -= 1
            
            
        # no need to return s 
        # as modified in-place
