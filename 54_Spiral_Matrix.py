from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # O(mn) time
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        
        direction = 'right'
        if right == 0:
            direction = 'down'
        
        ans = [matrix[0][0]]
        if right == 0 and bottom == 0:
            return ans
        
        x, y = 0, 0
        while left <= right and top <= bottom:
            if direction == 'right':
                y += 1
                ans.append(matrix[x][y])
                if y == right:
                    direction = 'down'
                    top += 1
            elif direction == 'down':
                x += 1
                ans.append(matrix[x][y])
                if x == bottom:
                    direction = 'left'
                    right -= 1
            elif direction == 'left':
                y -= 1
                ans.append(matrix[x][y])
                if y == left:
                    direction = 'top'
                    bottom -= 1
            else:
                x -= 1
                ans.append(matrix[x][y])
                if x == top:
                    direction = 'right'
                    left += 1
        return ans

sol = Solution()
print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(sol.spiralOrder([[2]]))
print(sol.spiralOrder([[1,2,3,4]]))
print(sol.spiralOrder([[1],[2],[3], [4]]))
