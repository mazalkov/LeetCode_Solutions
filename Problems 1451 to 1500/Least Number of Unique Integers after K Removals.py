class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
      
        for i, v in enumerate(sorted(counter.values())):
            k -= v
            if k < 0:
                return len(counter) - i
              
        return 0
