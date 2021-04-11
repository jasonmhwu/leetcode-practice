from typing import List

class Solution:
    def __init__(self):
        self.longest_path_each_cell = []
        self.longest_path = 1
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # pick a node -> start to walk in increasing paths
        # longestPath[i][j] == longest path start from node i, j
        # O(n**2) time, O(n**2) memory
        def findIncreasingPath(i, j):
            '''find all increasing paths from (i, j) and return result to longest_path_each_cell.'''
            self.longest_path_each_cell[i][j] = 1
            direc = ((0, 1), (0, -1), (1, 0), (-1, 0))
            for d in direc:
                next_x, next_y = i + d[0], j + d[1]
                if 0 <= next_x < m\
                    and 0 <= next_y < n\
                    and matrix[next_x][next_y] > matrix[i][j]:
                    if self.longest_path_each_cell[next_x][next_y] < 0:
                        findIncreasingPath(next_x, next_y)
                    self.longest_path_each_cell[i][j] = max(
                        self.longest_path_each_cell[i][j],
                        1 + self.longest_path_each_cell[next_x][next_y]
                    )
            self.longest_path = max(self.longest_path, self.longest_path_each_cell[i][j])
        
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            self.longest_path_each_cell.append([-1] * n)
        
        for i in range(m):
            for j in range(n):
                if self.longest_path_each_cell[i][j] < 0:
                    findIncreasingPath(i, j)
        return self.longest_path

