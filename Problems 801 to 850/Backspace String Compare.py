from typing import List


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        def reduce(x: str) -> List[str]:
            x_stack = []
            for char in x:
                if char == "#":
                    if x_stack:
                        x_stack.pop()
                else:
                    x_stack.append(char)

            return x_stack
        
        s_reduced = reduce(s)
        t_reduced = reduce(t)

        return s_reduced == t_reduced
