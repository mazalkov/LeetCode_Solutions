# https://leetcode.com/problems/unique-number-of-occurrences

# Runtime: 57 ms, faster than 73.19% of Python3 online submissions for Unique Number of Occurrences.
# Good runtime, there may be a more efficient, manual approach, but the Counter object handles complexity.

# Memory Usage: 13.8 MB, less than 97.26% of Python3 online submissions for Unique Number of Occurrences.
# Near perfect memory usage, a Counter is relatively 'cheap' in terms of memory, res variable can be garbage collected.


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        c = Counter(arr)
        vals = c.values()
        res = len(vals) == len(set(vals))
        
        
        return res
