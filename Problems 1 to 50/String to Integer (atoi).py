class Solution:
    def myAtoi(self, s: str) -> int:
        
        s = s.lstrip()
        sign = 0
        
        if s:
            if s[0] == '-':
                sign = -1
                s = s[1:]
                
            elif s[0] == '+':
                sign = 1
                s = s[1:]
                
            else:
                sign = 1
        
        else:
            return 0
        
        unsigned_res = ""
        
        while s:
            if s[0].isnumeric():
                unsigned_res += s[0]
                s = s[1:]
            else:
                break
                
        unsigned_res = int(unsigned_res) if unsigned_res else 0
        
        res = sign * unsigned_res
                
        if res < -2 ** 31:
            return -2 ** 31
        
        elif res > 2**31 - 1:
            return 2**31 - 1
        
        else:
            return res
