# https://leetcode.com/problems/pascals-triangle-ii

# Runtime: 28 ms, faster than 89.56% of Python3 online submissions for Pascal's Triangle II.
# Surprisingly fast considering I'm manually creating lists, rather than using O(1) calculations

# Memory Usage: 14.2 MB, less than 77.55% of Python3 online submissions for Pascal's Triangle II.
# Very memory efficient somehow, even though the lists are being appended each time, not sure why it's so good.


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        l = []
        
        for i in range(rowIndex+1):
            temp_l = []
            
            # create a list of lists of every row up to the index
            for j in range(i+1):
                temp_l.append(factorial(i) // (factorial(j)*factorial(i-j)) )
            l.append(temp_l)
            
        # return only the last list
        return l[-1]
