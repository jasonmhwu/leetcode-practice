import heapq
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # at least O(n)
        # brute force: sort nums and get ans in a single pass, O(nlogn) time, O(n) space
        # approach 2: throw away non-positive numbers, form a heap. O(n) time and space
        nums_pos = list(filter(lambda n: n > 0, nums))
        heapq.heapify(nums_pos)
        ans = 1
        while nums_pos:
            if (min_num := heapq.heappop(nums_pos)) == ans:
                ans += 1
            elif min_num > ans:
                return ans
            else:
                continue
        return ans

sol = Solution()
print(sol.firstMissingPositive([0,1,1,2,2]))
