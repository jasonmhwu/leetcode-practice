from typing import List
import bisect



class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # do binary search on first column, then do binary search on the answer row
        # O(logmn) time, O(1) space
        i = bisect.bisect_left(next(zip(*matrix)), target)
        if i < len(matrix) and matrix[i][0] == target:
            return True
        else:
            j = bisect.bisect_left(matrix[i-1], target)
        return matrix[i-1][j] == target if j < len(matrix[0]) else False

sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
