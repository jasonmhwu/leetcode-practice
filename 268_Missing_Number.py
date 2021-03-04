from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (len(nums)+1) * (len(nums)) // 2 - sum(nums)

sol = Solution()
print(sol.missingNumber([0]))
print(sol.missingNumber([0, 1]))
print(sol.missingNumber([0, 3, 1]))

