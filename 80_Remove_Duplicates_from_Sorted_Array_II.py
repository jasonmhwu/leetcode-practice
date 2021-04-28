from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # one-pass, use two pointers to record the traversal of the old and new nums
        # O(n) time, O(1) space
        new_ptr, ctr = 1, 1
        for i in range(1, len(nums)):
            if (nums[i] == nums[i-1] and ctr < 2) or (nums[i] != nums[i-1]):
                ctr = 2 if nums[i] == nums[i-1] else 1
                nums[new_ptr] = nums[i]
                new_ptr += 1
        return new_ptr

sol = Solution()
print(sol.removeDuplicates([0,0,1,1,1,1,2,2,3]))
