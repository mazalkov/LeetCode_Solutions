# https://leetcode.com/problems/distribute-candies

# Runtime: 917 ms, faster than 69.50% of Python3 online submissions for Distribute Candies.
# Pretty good runtime, taking the lengths of a set and its hashed version may be quite slow.

# Memory Usage: 16.3 MB, less than 47.65% of Python3 online submissions for Distribute Candies.
# Not great memory usage but not sure why, only taking the minimum of two lengths, maybe hashing is larger?


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        
        # not completely sure why it works but got it in the end
        return min(len(candyType)//2, len(set(candyType)))
