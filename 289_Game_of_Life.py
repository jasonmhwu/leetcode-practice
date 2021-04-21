from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # in-place solution
        # add 10 if board[i][j] lives in next state
        # map each cell to b // 10
        # O(n**2) time, O(1) space
        def willLive(i, j) -> int:
            """Determine whether cell(i, j) will live in the next state."""
            direc = (
                (1, 1),
                (1, 0),
                (1, -1),
                (0, 1),
                (0, -1),
                (-1, 1),
                (-1, 0),
                (-1, -1),
            )
            num_live_neighbors = 0
            for dx, dy in direc:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] % 10:
                    num_live_neighbors += 1
            if board[i][j] % 10:
                board[i][j] += 10 if num_live_neighbors in [2, 3] else 0
            else:
                board[i][j] += 10 if num_live_neighbors == 3 else 0
            
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                willLive(i, j)
        for i in range(m):
            board[i] = [b // 10 for b in board[i]]

sol = Solution()
print(sol.gameOfLife([[1,1],[1,0]]))
