from typing import List
from collections import Counter


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # O(n) space,  O(n) time
        nums_counter = Counter(nums)
        for k, v in nums_counter.items():
            if v > 1:
                return k

sol = Solution()
print(sol.findDuplicate([2,2,2,2,2]))
print(sol.findDuplicate([1,3,4,2,2]))
