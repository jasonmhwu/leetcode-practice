from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # O(NM) time, O(N) space
        # 2-D dp approach
        if not prices:
            return 0
        dp_curr, dp_prev = [0] * len(prices), [0] * len(prices)
        max_profit = 0
        ans = 0
        for _ in range(k):
            max_profit = -prices[0]
            for i in range(1, len(prices)):
                dp_curr[i] = max(dp_curr[i-1], prices[i] + max_profit)
                max_profit = max(max_profit, dp_prev[i-1] - prices[i])
            ans = max(ans, dp_curr[-1])
            dp_prev = dp_curr
            dp_curr = [0] * len(prices)
        return ans
                
sol = Solution()
print(sol.maxProfit(2, [3,2,6,5,0,3]))
