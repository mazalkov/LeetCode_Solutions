class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        LENGTH = len(arr)
        QUARTER = LENGTH // 4

        for i in range(LENGTH-QUARTER):
            if arr[i] == arr[i+QUARTER]:
                return arr[i]
