from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # solution 1:  O(n) time, O(n) space
        # return Counter(nums).most_common(1)[0][0]
        # solution 2: Boyer-Moore Voting algorithm
        elm, ctr = 0, 0
        for n in nums:
            if ctr == 0:
                elm = n
                ctr += 1
            else:
                ctr += 1 if elm == n else -1
        return elm

sol = Solution()
print(sol.majorityElement([2,2,1,1,1,2,2]))
print(sol.majorityElement([3,2,3]))
