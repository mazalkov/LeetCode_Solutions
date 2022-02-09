# https://leetcode.com/problems/fizz-buzz

# Runtime: 40 ms, faster than 91.88% of Python3 online submissions for Fizz Buzz.
# Very fast speed, although there may be a faster way to check divisibility via bits.

# Memory Usage: 14.9 MB, less than 90.14% of Python3 online submissions for Fizz Buzz.
# Excellent memory usage, not defining unnecessary variables, only storing temporary results.


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        answer = []
        
        for i in range(1, n+1):
            
            if (i % 3 == 0) and (i % 5 == 0):
                answer.append("FizzBuzz")
                
            elif (i % 5 == 0):
                answer.append("Buzz")
                
            elif (i % 3 == 0):
                answer.append("Fizz")
                
            else:
                answer.append(str(i))
                
                
        return answer
