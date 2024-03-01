class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:

        ones = s.count("1")
        zeros = len(s) - ones

        if ones == 1:
            return f'{"0"*zeros}{"1"}'

        res = f'{"1"*(ones-1)}{"0"*zeros}{"1"}'

        return res
