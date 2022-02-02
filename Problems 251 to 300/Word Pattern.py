# https://leetcode.com/problems/word-pattern

# Runtime: 43 ms, faster than 50.30% of Python3 online submissions for Word Pattern.
# Happy with the runtime, dicts should be fast but I feel my if-else structure is verbose, unsure how to reduce.

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
                
                else:
                    seen[char] = words[i]
                
        
        return True
