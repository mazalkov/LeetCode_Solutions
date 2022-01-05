from math import factorial


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        l = []
        
        for i in range(numRows):
            temp_l = []
            
            for j in range(i+1):
                temp_l.append(factorial(i) // (factorial(j)*factorial(i-j)) )
            l.append(temp_l)
            
            
        return l
