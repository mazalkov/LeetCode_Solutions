# https://leetcode.com/problems/top-k-frequent-words

# Runtime: 62 ms, faster than 90.52% of Python3 online submissions for Top K Frequent Words.
# Excellent runtime, using a Counter and then sorting a set of the words appears to be efficient

# Memory Usage: 13.9 MB, less than 94.18% of Python3 online submissions for Top K Frequent Words.
# Excellent memory usage, storing a list of a set isn't too bad and nothing else is really needed


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # thanks to multiple sources
        
        lookup = collections.Counter(words)
        words = list(set(words))
        words.sort(key = lambda w: (-lookup[w], w))
        
        
        return words[:k]
