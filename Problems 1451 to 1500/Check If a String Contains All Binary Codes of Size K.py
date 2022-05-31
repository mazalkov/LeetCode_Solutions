# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k

# Runtime: 591 ms, faster than 38.49% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
# Poor runtime, this method constantly sets values even when they have been set before, should use a hash-set to be quicker.

# Memory Usage: 21.9 MB, less than 94.25% of Python3 online submissions for Check If a String Contains All Binary Codes of Size K.
# Excellent memory usage, the static array is already defined and so only the intermediate index variable is left for readability.


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # could be improved with: https://youtu.be/qU32rTy_kOM
        
        array = [False] * (2**k)
        
        for i in range(0, len(s)-k+1):
            index = int(s[i:i+k], 2) 
            array[index] = True
            

        return all(array)
