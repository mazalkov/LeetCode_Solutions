from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        
        c = Counter(s).most_common()

        return "".join(char * count for char, count in c)
