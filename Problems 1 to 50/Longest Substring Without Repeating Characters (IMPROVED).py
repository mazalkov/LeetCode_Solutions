# https://leetcode.com/problems/longest-substring-without-repeating-characters

# Runtime: 68 ms, faster than 82.76% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Good runtime, sliding window should be quicker than checking for membership of a set on each iteration, while loop could be improved.

# Memory Usage: 14 MB, less than 93.04% of Python3 online submissions for Longest Substring Without Repeating Characters.
# Excellent memory usage, only having to store the left pointer, as well as the hash set, but latter is necessary for this.


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # thanks to: https://youtu.be/wiGpQwVHdE0
        
        seen = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
                
            seen.add(s[r])
            res = max(res, r-l+1)
            
            
        return res
