from typing import List


class Solution:
    def __init__(self):
        self._memo = dict()
        
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dynamic programming
        # dp[i] = sum_j (dp[i-nums[j]])
        # use memoization
        # O(T*N) time, O(T + N) space, T == target value, N == len(nums)
        if target in self._memo.keys():
            return self._memo[target]
        ans = sum([self.combinationSum4(nums, target - n) for n in nums if target > n])
        ans += 1 if target in nums else 0
        self._memo[target] = ans
        return ans
        
sol = Solution()
print(sol.combinationSum4([1,2,3], 4))
