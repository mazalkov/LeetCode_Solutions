class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        c = collections.Counter(nums)
        
        
        return [k for k, v in c.most_common(k)]
