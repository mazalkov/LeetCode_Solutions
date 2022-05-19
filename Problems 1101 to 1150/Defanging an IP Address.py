# https://leetcode.com/problems/defanging-an-ip-address

# Runtime: 39 ms, faster than 57.77% of Python3 online submissions for Defanging an IP Address.
# Average runtime, just using Python's built-in replace isn't very efficient perhaps, could be faster?

# Memory Usage: 13.7 MB, less than 99.85% of Python3 online submissions for Defanging an IP Address.
# Excellent memory usage, using a built-in may be slower but at least the memory is handled more efficiently.


class Solution:
    def defangIPaddr(self, address: str) -> str:
        
        return address.replace(".", "[.]")
