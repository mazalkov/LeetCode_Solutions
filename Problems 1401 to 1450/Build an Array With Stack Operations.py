class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        res = []
        i, current = 0, 1

        while current <= n:
            if i == len(target):
                return res

            elif target[i] == current:
                res.append("Push")
                i += 1

            else:
                res.append("Push")
                res.append("Pop")

            current += 1

        return res
