# https://leetcode.com/problems/word-pattern

# Runtime: 24 ms, faster than 97.95% of Python3 online submissions for Word Pattern.
# Got rid of the final else check for seen[char] = words[i], now runtime is very fast.

# Memory Usage: 13.9 MB, less than 99.41% of Python3 online submissions for Word Pattern.
# Very happy with memory usage, only creating a dict and list of split words is highly space saving.


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        seen = {}
        words = s.split()
        
        if len(pattern) != len(words):
            return False
        
        for i, char in enumerate(pattern):
            
            if char in seen:
                if seen[char] != words[i]:
                    return False
            
            else:
                if words[i] in seen.values():
                    return False
                
            seen[char] = words[i]
                
        
        return True
