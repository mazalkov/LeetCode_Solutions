# https://leetcode.com/problems/longest-common-prefix/

# Runtime: 28 ms, faster than 93.56% of Python3 online submissions for Longest Common Prefix.
# Pretty decent runtime since there's not as much list/string traversal.

# Memory Usage: 14.1 MB, less than 99.56% of Python3 online submissions for Longest Common Prefix.
# Very good memory usage, only storing a few variables and doing minimal iterations.


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        if not strs:
            return ""

        min_s = min(strs)
        max_s = max(strs)
        
        if not min_s:
            return ""
        
        for i in range(len(min_s)):
            if max_s[i] != min_s[i]:
                return max_s[:i]
            
        return min_s
