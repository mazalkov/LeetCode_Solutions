# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

# Runtime: 52 ms, faster than 99.18% of Python3 online submissions for Two Sum II - Input Array Is Sorted.
# Think I got lucky with caching on this particular runtime, but very happy with it, my best % so far!

# Memory Usage: 14.6 MB, less than 87.22% of Python3 online submissions for Two Sum II - Input Array Is Sorted.#
# Wasn't sure how good memory would be because of the creation of the idx1, idx2, variables, but still great as well


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = set()
        
        for elem in numbers:
            if target - elem not in seen:
                seen.add(elem)
                
            else:
                idx1 = numbers.index(target-elem)+1
                idx2 = numbers.index(elem)+1
                
                if idx1 == idx2:
                    idx2 += 1
                    
                    
                return [idx1, idx2]
