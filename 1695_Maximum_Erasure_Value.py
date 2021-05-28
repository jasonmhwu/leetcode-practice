from itertools import accumulate
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        # calculate accumulative sum array
        # for each num i, find the last identical number j, update max sum using cumsum[i] - cumsum[j]
        # keep dictionary of num -> last_index
        # O(N) time, O(N) space
        prev_occured = dict()
        cumsum = list(accumulate(nums))
        ans = nums[0]
        head = 0
        for i in range(len(nums)):
            prev_index = prev_occured.get(nums[i], -1)
            while prev_index >= head:
                prev_occured.pop(nums[head])
                head += 1
            prev_occured[nums[i]] = i
            ans = max(ans, cumsum[i] - (cumsum[head-1] if head > 0 else 0))
        return ans

sol = Solution()
print(sol.maximumUniqueSubarray([5,6,1,2,5,3,4]))
