class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        LENGTH = len(temperatures)
        stack = []
        res = [0] * LENGTH

        for i, temp in enumerate(temperatures):
            while stack and (temp > temperatures[stack[-1]]):
                prev_idx = stack.pop()
                res[prev_idx] = i - prev_idx
            
            stack.append(i)

        return res
