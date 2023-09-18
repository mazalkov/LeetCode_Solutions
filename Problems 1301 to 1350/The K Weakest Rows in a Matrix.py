class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        lookup = dict()

        for i, row in enumerate(mat):
            total = sum(row)
            lookup[i] = total
        
        return sorted(lookup, key=lookup.get)[:k]
