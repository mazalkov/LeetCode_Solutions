class Solution:
    def romanToInt(self, s: str) -> int:
        
        total = 0
        
        d = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        
        for i in range(len(s)-1, -1, -1):
            
            seen = d[s[i]]
            
            if 3 * seen < total:
                total -= seen
            else:
                total += seen
                
                
        return total
