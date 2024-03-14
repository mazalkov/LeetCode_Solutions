from collections import Counter


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        freqs = Counter()
        freqs[0] = 1
        count, prefix = 0, [0]

        for n in nums:
            last = prefix[-1] + n
            prefix.append(last)

            count += freqs[last-goal]
            freqs[last] += 1

        return count
