class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:

        if len(arr) < 3:
            return False

        elif len(arr) == 3:
            return all(x % 2 != 0 for x in arr)

        for i, num in enumerate(arr[:-2]):
            if all(x % 2 != 0 for x in arr[i:i+3]):
                return True
