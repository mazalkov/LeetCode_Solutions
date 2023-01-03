# https://leetcode.com/problems/delete-columns-to-make-sorted

# Runtime: 314ms, Beats: 52%
# Average runtime, using the joining functions and checking whole strings is likely the cause of this.

# Memory: 14.6MB, Beats: 61.89%
# Good memory usage, could compare element by element instead of the whole string at once instead.


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:

        res = 0
        width = len(strs[0])

        for i in range(width):
            check_string = "".join([x[i] for x in strs])
            sorted_string = "".join(sorted(check_string))

            if check_string != sorted_string:
                res += 1


        return res
