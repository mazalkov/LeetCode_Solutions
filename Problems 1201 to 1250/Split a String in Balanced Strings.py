# https://leetcode.com/problems/split-a-string-in-balanced-strings

# Runtime: 28ms, Beats: 93.27%
# Near perfect runtime, thank you to suggestions from @RobbieMarseglia.

# Memory: 13.7MB, Beats: 96.95%
# Near perfect memory usage, thank you to suggestions from @RobbieMarseglia.


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        res = 0
        counter = 0

        for c in s:
            if c == "L":
                counter -= 1

            else:
                counter += 1

            if counter == 0:
                res += 1


        return res
