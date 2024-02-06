from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))
            lookup[key].append(string)

        return list(lookup.values())
