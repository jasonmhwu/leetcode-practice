import bisect
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # do two binary search on target - 0.5 and target + 0.5
        left = bisect.bisect(nums, target-0.5)
        right = bisect.bisect(nums, target+0.5) - 1
        if right == left - 1:
            return [-1, -1]
        else:
            return [left, right]
        
sol = Solution()
print(sol.searchRange([5,7,7,8,8,10], 8))
print(sol.searchRange([5,7,7,8,8,10], 6))
print(sol.searchRange([], 0))
