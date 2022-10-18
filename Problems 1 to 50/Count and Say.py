# https://leetcode.com/problems/count-and-say

# Runtime: 67 ms, faster than 73.58% of Python3 online submissions for Count and Say.
# Good runtime, wasn't sure of a "clean" algorithm to use but this one seems efficient

# Memory Usage: 13.8 MB, less than 86.43% of Python3 online submissions for Count and Say.
# Excellent memory usage, only storing a few temporary variables inbetween loops.


class Solution:
    def countAndSay(self, n: int) -> str:
    # thanks to: https://wangyy395.medium.com/leetcode-38-count-and-say-78730a482aef    
        
        res = '1'
        for _ in range(1, n):
            prev, count = '.', 0
            curr_str = ""
            for char in res:
                if char == prev or prev == '.':
                    count += 1
                else:
                    curr_str += str(count) + prev
                    count = 1
                prev = char
            curr_str += str(count) + prev
            res = curr_str
        return res
