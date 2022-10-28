# https://leetcode.com/problems/group-anagrams

# Runtime: 213 ms, faster than 53.62% of Python3 online submissions for Group Anagrams.
# Average runtime, sorting each string maybe isn't very efficient but not sure how otherwise.

# Memory Usage: 17.7 MB, less than 67.00% of Python3 online submissions for Group Anagrams.
# Good memory usage, storing a dict isn't intensive, sorting and joining may in fact be though.


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groupings = dict()
        
        for s in strs:
            sort = ''.join(sorted(s))
            
            if sort in groupings:
                groupings[sort].append(s)
                
            else:
                groupings[sort] = [s]
                
                
        return groupings.values()
