from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dynamic programming
        # dp[i][j] = dp[i][j-1] + dp[i-1][j] if they are spaces
        # O(MN) time, O(n) space
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [1] + [0] * (n-1)
        for i in range(m):
            if obstacleGrid[i][0]:
                dp[0] = 0
            for j in range(1, n):
                dp[j] = dp[j] + dp[j-1] if obstacleGrid[i][j] == 0 else 0
        return dp[-1]
    
sol = Solution()
print(sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))
