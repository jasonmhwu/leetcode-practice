from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # brute force: O(n**2) total subarrays * O(n) sum operation
        # keep track of subarray sums until entry i: reduce to O(n**2) time
        # TLE
        # use hashmap to store the trailing cum_sum
        
        ans = 0
        cum_sum = 0
        sum_dict = defaultdict(int)
        for n in nums:
            cum_sum += n
            ans += sum_dict[cum_sum - k]
            sum_dict[cum_sum] += 1
        return ans + sum_dict[k]
        
sol = Solution()
print(sol.subarraySum([1,1,1], 2))
print(sol.subarraySum([1,2,3], 3))
print(sol.subarraySum([1], 0))
