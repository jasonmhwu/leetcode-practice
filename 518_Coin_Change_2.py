from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins = sorted(coins, reverse=True)
        # dp[i] = unique ways to reach amount i
        # dp[0] = 1
        # O(N*M) time, O(N) memory, N = amount, M = number of coins
        
        dp = [1] + [0] * amount
        for c in coins:
            for i in range(1, amount+1):
                if i >= c:
                    dp[i] += dp[i-c]
        return dp[-1]

sol = Solution()
print(sol.change(5, [1,2,5]))
print(sol.change(20, [2,4,1,5]))
