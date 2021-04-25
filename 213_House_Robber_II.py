from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # if you rob first house, throw away first and last house
        # if you don't rob first house, throw away first house only
        # reduces into two linear house robber problem
        # dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        # O(n) time, O(1) space
        def dp_list(nums: List[int]) -> int:
            if not nums:
                return 0
            elif len(nums) == 1:
                return nums[0]
            else:
                dp = [nums[0], max(nums[0], nums[1])]
                for n in nums[2:]:
                    dp[0], dp[1] = dp[1], max(dp[1], dp[0] + n)
                return max(dp)
        
        return max(nums[0] + dp_list(nums[2:-1]), dp_list(nums[1:]))

sol = Solution()
print(sol.rob([1,2,3,1]))
print(sol.rob([1]))
