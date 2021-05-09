from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # keep three numbers: maximum sum % 3 == 0, 1, 2
        # O(n) time, O(1) space 
        max_sum = [0,0,0]
        for n in nums:
            tmp_sum = [n + m for m in max_sum]
            for m in tmp_sum:
                max_sum[m%3] = max(max_sum[m%3], m)
        return max_sum[0]

sol = Solution()
print(sol.maxSumDivThree([1,2,3,4,4]))
