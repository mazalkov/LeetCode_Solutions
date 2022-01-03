class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        for i in range(len(digits)-1, -1, -1):
            
            if digits[i] < 9:
                digits[i] += 1
                return digits
                
            else:
                digits[i] = 0
                
                
        # if we have looped through and not yet returned
        # all digits were '9's, so append a '1' to front
        digits.insert(0, 1)
        return digits
