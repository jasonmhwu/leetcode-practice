from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp problem
        # dp[i] = fewest number of coins to make up amount i
        # base case: dp[0] = 0
        # dp[i] = min(dp[i-c[j]] + 1)
        
        dp = [-1] * (amount+1)
        dp[0] = 0
        
        for a in range(1, amount+1):
            min_coins = 10**5
            for c in coins:
                if (a - c >= 0) and (dp[a-c] + 1 < min_coins):
                    min_coins = dp[a-c] + 1
            dp[a] = min_coins
        return dp[-1] if dp[-1] < 10 ** 5 else  -1
                   
sol = Solution()
print(sol.coinChange([1,2,5], 11))
print(sol.coinChange([1], 0))
print(sol.coinChange([2], 1))
 
