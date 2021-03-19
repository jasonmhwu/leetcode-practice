from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # one-pass through nums and record the sign of the previous difference
        # also record the last "transition number"
        # O(n) time, O(1) memory
        if len(nums) == 1:
            return len(nums)
        if len(nums) == 2:
            return 1 if nums[0] == nums[1] else 2
        
        max_length = 1
        is_increasing = 0
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] or (nums[i] - nums[i-1]) * is_increasing > 0:
                continue
            elif is_increasing == 0:
                is_increasing = 1 if nums[i] > nums[i-1] else -1
                max_length += 1
            else:
                max_length += 1
                is_increasing *= -1
        return max_length

sol = Solution()
print(sol.wiggleMaxLength([1,4,3,8,2,6]))
print(sol.wiggleMaxLength([1,1,1,1]))
