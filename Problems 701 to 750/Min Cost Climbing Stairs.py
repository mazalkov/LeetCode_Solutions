class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        LENGTH = len(cost)
        
        for i in range(2, LENGTH):
            cost[i] += min(cost[i-1], cost[i-2])

        return min(cost[LENGTH-1], cost[LENGTH-2])
