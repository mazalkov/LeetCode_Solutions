class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        LENGTH = len(pref)
        arr = [None] * LENGTH
        arr[0] = pref[0]

        for i in range(1, LENGTH):
            arr[i] = pref[i-1] ^ pref[i]

        return arr
