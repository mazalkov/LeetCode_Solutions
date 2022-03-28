# https://leetcode.com/problems/robot-return-to-origin

# Runtime: 30 ms, faster than 98.76% of Python3 online submissions for Robot Return to Origin.
# Excellent runtime, doing multiple passes to count occurences may have variable behaviour though.

# Memory Usage: 14.1 MB, less than 91.05% of Python3 online submissions for Robot Return to Origin.
# Excellent memory usage, no need to define or store unnecessary variables, just count and compare.


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        
        # robot returns if left moves equal right moves AND down moves equal up moves
        return (moves.count("L") == moves.count("R")) and (moves.count("D") == moves.count("U"))
