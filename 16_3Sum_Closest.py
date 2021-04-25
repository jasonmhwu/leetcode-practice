from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # two pointer approach
        # O(n**2) time, O(n) space
        nums = sorted(nums)
        ans_diff = 10**5
        for idx, n in enumerate(nums[:-2]):
            left, right = idx+1, len(nums)-1
            while left < right:
                curr_diff = n + nums[left] + nums[right] - target
                if curr_diff == 0:
                    return target
                if abs(curr_diff) < abs(ans_diff):
                    ans_diff = curr_diff
                if curr_diff < 0:
                    left += 1
                if curr_diff > 0:
                    right -= 1
        return target + ans_diff
    
sol = Solution()
print(sol.threeSumClosest([-1, -4, 1, 2], 1))
