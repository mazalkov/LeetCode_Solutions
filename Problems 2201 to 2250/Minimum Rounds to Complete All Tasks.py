# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks

# Runtime: 1702 ms, Beats: 48.4%
# Average runtime, there are likely more sophisticated solutions with data structures, but this works.

# Memory: 28.5 MB, Beats: 31.54%
# Below average memory usage, not sure why as the Counter should be relatively efficient, can investigate.


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:

        rounds = 0

        c = Counter(tasks)
        freqs = list(c.values())

        for freq in freqs:
            if freq == 1:
                return -1
            
            elif freq < 4:
                rounds += 1

            elif freq % 3 == 0:
                rounds += freq // 3

            else:
                rounds += (freq // 3) + 1


        return rounds
