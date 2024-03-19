from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        LENGTH = len(tasks)
        if n == 0:
            return LENGTH

        freqs = Counter(tasks)
        max_freq = max(freqs.values())
        num_max_freqs = list(freqs.values()).count(max_freq)
        
        minimum = (max_freq - 1) * (n + 1) + num_max_freqs

        return max(minimum, len(tasks))
