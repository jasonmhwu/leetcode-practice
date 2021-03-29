from collections import defaultdict
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # dp approach
        # dp[i] = minimum cost  up till day i
        # dp[i] = min(cost[0] +  dp[i-1], cost[1] + dp[i-7], cost[2] + dp[i-30])
        # O(N) time, O(N) space
        dp = defaultdict(int)
        for i in range(len(days)):
            for j in range(days[i-1]+1, days[i]):
                dp[j] = dp[days[i-1]]
            
            dp[days[i]] = min(
                costs[0] + dp[days[i]-1],
                costs[1] + dp[days[i]-7],
                costs[2] + dp[days[i]-30]
            )
        return dp[days[-1]]

sol = Solution()
print(sol.mincostTickets([1,4,6,7,8,20], [2,7,15]))
