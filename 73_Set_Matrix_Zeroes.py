from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # two-pass through the matrix
        # when encounter 0, set all non-zero element in row and column to 0.5
        # second pass: set 0.5 to 0
        m = len(matrix)
        n = len(matrix[0])
        for idx, row in enumerate(matrix):
            if 0 in row:
                matrix[idx] = [0.5 if n != 0 else 0 for n in row]
        for idx, col in enumerate(zip(*matrix)):
            if 0 in col:
                for j in range(m):
                    matrix[j][idx] = 0
            else:
                for j in range(m):
                    if matrix[j][idx] == 0.5:
                        matrix[j][idx] = 0

sol = Solution()
print(sol.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
