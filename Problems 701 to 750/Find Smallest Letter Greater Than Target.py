class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        LENGTH = len(letters)
        left, right = 0, LENGTH-1

        result = letters[0]

        while left <= right:
            mid = (left + right) // 2

            if target < letters[mid]:
                result = letters[mid]
                right -= 1

            else:
                left += 1


        return result
