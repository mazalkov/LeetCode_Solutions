# https://leetcode.com/problems/length-of-last-word/

# Runtime: 28 ms, faster than 76.72% of Python3 online submissions for Length of Last Word.
# Adequate runtime, although there will be a number of ways to quicken the process.

# Memory Usage: 14.4 MB, less than 36.14% of Python3 online submissions for Length of Last Word.
# Reversing the list likely uses a lot of memory, but I can't seem to traverse it in reverse.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        # strip the string of spaces and check if the result is empty, if it is return 0
        if not s.strip():
            return 0
        
        else:
            # split the string into a list
            split_list = s.split(" ")
            
            # reverse the list for easier traversal
            split_list = split_list[::-1]
            
            # starting from the "end" of the original list
            for i in range(len(s)):
                # output the first non-empty element and break
                if len(split_list[i]) > 0:
                    return len(split_list[i])
                    break
