# https://leetcode.com/problems/happy-number

# Runtime: 42 ms, faster than 42.16% of Python3 online submissions for Happy Number.
# Pretty average speed, I used a list comprehension which is probably quite slow.

# Memory Usage: 14.3 MB, less than 48.63% of Python3 online submissions for Happy Number.
# Space should be used efficiently, although again the list comp may not be the best for this.


class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        
        while n not in seen:
            seen.add(n)
            n = sum(int(c)**2 for c in str(n))

            
        return n == 1
