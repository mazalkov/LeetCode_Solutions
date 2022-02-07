# https://leetcode.com/problems/ransom-note

# Runtime: 40 ms, faster than 94.77% of Python3 online submissions for Ransom Note.
# Very good speed, only creating two Counters and then finding the difference.

# Memory Usage: 14.2 MB, less than 75.81% of Python3 online submissions for Ransom Note.
# Not sure why the memory usage isn't as high, perhaps there is a more linear approach.


from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        
        return not Counter(ransomNote) - Counter(magazine)
