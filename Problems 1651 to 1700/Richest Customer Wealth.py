class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        res = max([sum(row) for row in accounts])
        return res
