class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        LENGTH1, LENGTH2 = len(text1), len(text2)

        is_cached = [[False] * LENGTH2 for _ in range(LENGTH1)]
        cache = [[None] * LENGTH2 for _ in range(LENGTH1)]

        def helper(idx1: int, idx2: int) -> int:
            if idx1 == LENGTH1 or idx2 == LENGTH2:
                return 0

            if is_cached[idx1][idx2]:
                return cache[idx1][idx2]

            longest_seq = max(
                helper(idx1 + 1, idx2),
                helper(idx1, idx2 + 1)
            )

            if text1[idx1] == text2[idx2]:
                longest_seq = max(
                    longest_seq,
                    helper(idx1 + 1, idx2 + 1) + 1
                )

            is_cached[idx1][idx2] = True
            cache[idx1][idx2] = longest_seq

            return longest_seq

        return helper(0, 0)
