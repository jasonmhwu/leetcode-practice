from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dp[i] = dp_prev[i-1] + dp_prev[i]
        # O(n) time, O(logn) space
        dp_prev = triangle[0]
        for layer in range(1, len(triangle)):
            dp_prev = [dp_prev[0] + triangle[layer][0]] + [
                min(dp_prev[i-1], dp_prev[i]) + triangle[layer][i]
                for i in range(1, layer)
            ] + [dp_prev[-1] + triangle[layer][-1]]
        return min(dp_prev)

sol = Solution()
print(sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
