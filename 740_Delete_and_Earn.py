from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_num = max(counter.keys())
        dp = [0] * (max_num+1)
        dp[1] = 1*counter[1]
        for i in range(2, max_num+1):
            dp[i] = max(dp[i-2] + i*counter[i], dp[i-1])
        return dp[-1]

sol = Solution()
print(sol.deleteAndEarn([3,4,2]))
print(sol.deleteAndEarn([1]))
