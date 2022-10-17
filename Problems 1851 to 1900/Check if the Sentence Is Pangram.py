# https://leetcode.com/problems/check-if-the-sentence-is-pangram

# Runtime: 51 ms, faster than 65.02% of Python3 online submissions for Check if the Sentence Is Pangram.
# Good runtime, it would be much faster to just check len(set(sentence)) == 26 but this is more rigorous

# Memory Usage: 13.8 MB, less than 95.55% of Python3 online submissions for Check if the Sentence Is Pangram.
# Excellent memory usage surprisingly, storing two sets doesn't seem to take that much more space than one


import string


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        
        return set(string.ascii_lowercase).issubset(set(sentence))
