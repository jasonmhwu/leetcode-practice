from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # greedy -> O(N) time
        max_profit = 0
        curr_min = 10 ** 6
        for p in prices:
            max_profit = max(p - curr_min, max_profit)
            curr_min = min(p, curr_min)
        return max_profit

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))
print(sol.maxProfit([2]))
