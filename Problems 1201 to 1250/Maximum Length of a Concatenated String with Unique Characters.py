# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters

# Runtime: 750 ms, faster than 19.03% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.
# Poor runtime, admittedly I didn't really understand the solution provided by NeetCode so need to revisit this.

# Memory Usage: 13.9 MB, less than 65.84% of Python3 online submissions for Maximum Length of a Concatenated String with Unique Characters.
# Good memory usage, storing a few Counters and a seen set isn't as intensive as what else could possibly work.


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        seen = set()
        
     
        def is_overlap(seen, string):
            c = Counter(seen) + Counter(string)
            return max(c.values()) > 1
        
        
        def backtrack(i):
            if i == len(arr):
                return len(seen)
            
            res = 0
            
            if not is_overlap(seen, arr[i]):
                for c in arr[i]:
                    seen.add(c)
                
                res = backtrack(i+1)
                
                for c in arr[i]:
                    seen.remove(c)
            
            return max(res, backtrack(i+1))
                    
                    
        return backtrack(0)
