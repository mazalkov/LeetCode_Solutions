class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        # not particularly readable but this is LeetCode
        return sum([1 if "++" in op else -1 for op in operations])
