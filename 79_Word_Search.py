from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # use a dfs approach
        # find all starting points, start dfs, and mark visited points along the way
        # should take O(m*n) time and O(m*n) space
        m = len(board)
        n = len(board[0])
        visited = []
        
        def dfs(start_pos, visited, word):
            if not word:
                return True
            start_x, start_y = start_pos
            for x, y in ((start_x-1, start_y),
                        (start_x+1,  start_y),
                        (start_x,  start_y-1),
                        (start_x, start_y+1)):
                if x >= 0 and x < m and y >= 0 and y < n\
                    and board[x][y] == word[0] and (x, y) not in visited:
                    visited.append((x, y))
                    if dfs((x, y), visited, word[1:]):
                        return True
                    else:
                        visited.pop()
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited.append((i, j))
                    if dfs((i, j), visited, word[1:]):
                        return True
                    else:
                        visited.clear()
        return False
                    
sol = Solution()
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"))
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SES"))
print(sol.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))
print(sol.exist([["A"]], "AA"))
print(sol.exist([["A"]], "A"))
print(sol.exist([["A"]], "S"))
