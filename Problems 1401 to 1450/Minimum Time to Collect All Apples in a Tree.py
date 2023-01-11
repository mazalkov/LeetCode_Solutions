# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree

# Time: 712ms, Beats: 83.33%
# Good time complexity, recursive dfs seems quick relative to bfs and/or iterative.

# Memory: 52.6MB, Beats: 54.49%
# Average memory usage, appending both parent and child isn't necessary except for LC testcase. 


class Solution:
    # thanks to NeetCode
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        adjacencies = { i:[] for i in range(n)}

        for parent, child in edges:
            adjacencies[parent].append(child)
            adjacencies[child].append(parent)


        def dfs(node, parent):
            steps = 0

            for child in adjacencies[node]:
                if child == parent:
                    continue
                steps_child = dfs(child, node)
                if steps_child or hasApple[child]:
                    steps += (2 + steps_child)
            
            return steps

        return dfs(0, 0)
