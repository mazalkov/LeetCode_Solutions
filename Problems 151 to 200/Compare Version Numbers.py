# https://leetcode.com/problems/compare-version-numbers

# Runtime: 28 ms, faster than 93.87% of Python3 online submissions for Compare Version Numbers.
# Very good runtime, defining revisions using ternary operators may be inefficient, but still readable.

# Memory Usage: 13.9 MB, less than 92.33% of Python3 online submissions for Compare Version Numbers.
# Surprisingly good memory usage, I have defined some variables which aren't necessary but included for readability. 


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        v1 = version1.split(".")
        v2 = version2.split(".")
        
        longer = max(len(v1), len(v2))

        for index in range(longer):
             
            rev1 = int(v1[index]) if index < len(v1) else 0
            rev2 = int(v2[index]) if index < len(v2) else 0

            if rev1 != rev2:
                return -1 if rev1 < rev2 else 1

            
        return 0
