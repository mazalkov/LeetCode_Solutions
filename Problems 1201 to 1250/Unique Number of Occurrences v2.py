from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        c = Counter(arr)
        vals = c.values()
        
        return len(vals) == len(set(vals))
