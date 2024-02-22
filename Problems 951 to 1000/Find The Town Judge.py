class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trusters = [0] * n
        trustees = [0] * n

        for x, y in trust:
            # one-indexed
            trusters[x-1] += 1
            trustees[y-1] += 1

        for i in range(n):
            if (trusters[i] == 0) and (trustees[i] == n-1):
                # one-indexed
                return i+1

        return -1
