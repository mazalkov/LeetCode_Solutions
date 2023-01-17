# https://leetcode.com/problems/flip-string-to-monotone-increasing

# Runtime: 260ms, Beats: 70.59%
# Good runtime, good algorithm which doesn't use DP or a recursive approach.

# Memory: 15MB, Beats: 72.55%
# Good memory usage, again not using DP so likely not too bad for memory.


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        zeros = s.count("0")
        ones = 0
        output = zeros
        
        for bit in s:
            if bit == "0":
                zeros -= 1
            if bit == "1":
                ones += 1
            output = min(output, zeros+ones)


        return output
            
