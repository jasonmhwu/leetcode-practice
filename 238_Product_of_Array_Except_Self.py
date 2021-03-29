from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # forward and  backward pass: only need to record the cumulative product of nums[:i], or nums[i:]
        # O(n) time, O(1) space
        ans = [1] * len(nums)
        cumulative_product = 1
        for i in range(len(nums)):
            ans[i] *= cumulative_product
            cumulative_product *= nums[i]
        cumulative_product = 1
        for i in range(len(nums))[::-1]:
            ans[i] *= cumulative_product
            cumulative_product *= nums[i]
        return ans

sol = Solution()
print(sol.productExceptSelf([1, 2, 3, 4]))
