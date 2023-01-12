# https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label

# Runtime: 2094ms, Beats: 94.23%
# Near perfect runtime, thanks to the recursive search approach.

# Memory: 193.1MB, Beats: 50%
# Average memory usage which doesn't change over time, space sacrificed for speed.


class Solution:
    # thanks to "Programming Live With Larry"
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:

        adjacencies = collections.defaultdict(list)

        for parent, child in edges:
            adjacencies[parent].append(child)
            adjacencies[child].append(parent)

        res = [None]*n

        def search(node, parent):
            freqs = [0]*26

            for child in adjacencies[node]:
                if child != parent:
                    f = search(child, node)

                    for i in range(26):
                        freqs[i] += f[i]

            freqs[ord(labels[node]) - 97] += 1 # ord("a") = 97
            res[node] = freqs[ord(labels[node]) - 97]
            return freqs


        search(0, 0)
        return res
