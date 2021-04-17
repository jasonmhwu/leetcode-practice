from  typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointers, one-pass
        # O(n) time, O(1) space
        new_idx = 0
        for n in nums:
            if n != val:
                nums[new_idx] = n
                new_idx += 1
        return new_idx

