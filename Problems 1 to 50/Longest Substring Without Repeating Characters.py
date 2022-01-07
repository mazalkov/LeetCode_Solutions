class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        visited = set()
        left_ptr = 0
        max_length = 0
        
        for right_ptr in range(len(s)):
            
            while s[right_ptr] in visited:
                visited.remove(s[left_ptr])
                left_ptr += 1
            
            visited.add(s[right_ptr])
            max_length = max(max_length, right_ptr-left_ptr+1)
            
        return max_length
