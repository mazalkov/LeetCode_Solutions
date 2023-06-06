class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        arr.sort()
        diff = arr[1] - arr[0]

        return all((second - first == diff) for first, second in zip(arr, arr[1:]))
