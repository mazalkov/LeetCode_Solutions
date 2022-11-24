# https://leetcode.com/problems/word-search

# Runtime: 36 ms, faster than 99.75% of Python3 online submissions for Word Search.
# Near perfect runtime, credit to Lulit999 on the video for the pre-search checks.

# Memory Usage: 13.9 MB, less than 93.63% of Python3 online submissions for Word Search.
# Excellent memory usage, doing the previous setup saves the already minimal usage later.


class Solution:
# thanks to NeetCode and a comment by Lulit999 on the video
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        
        visited = set()
        
        word_dict = Counter(word)
        board_dict = Counter(itertools.chain.from_iterable(board))
        
        if any (count > board_dict[char] for char, count in word_dict.items()):
            return False
        
        if board_dict[word[0]] > board_dict[word[-1]]:
            word = word[::-1]
        
        def search(r, c, i):
            if i == len(word):
                return True
            
            if r < 0 \
            or c < 0 \
            or r >= ROWS \
            or c >= COLS \
            or word[i] != board[r][c] \
            or (r, c) in visited:
                return False
            
            visited.add((r, c))
            
            res = (search(r+1, c, i+1) or \
                   search(r-1, c, i+1) or \
                   search(r, c+1, i+1) or \
                   search(r, c-1, i+1))
            
            visited.remove((r, c))
            return res
        
        
        for r in range(ROWS):
            for c in range(COLS):
                if search(r, c, 0):
                    return True
                
        return False
