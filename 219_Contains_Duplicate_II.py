from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # use a set to keep track of last k numbers
        # if to-be-added item is already in set, return True
        # O(n) time, O(k) space
        last_k = set()
        for i, n in enumerate(nums):
            if i > k:
                last_k.remove(nums[i-k-1])
            if n in last_k:
                return True
            last_k.add(n)
        return False

sol = Solution()
print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2))
