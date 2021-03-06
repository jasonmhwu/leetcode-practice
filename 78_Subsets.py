from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # recursive approach
        # should take O(2**n) time and space
        if len(nums) == 1:
            return [[], nums]
        
        ans = []
        sublist = self.subsets(nums[1:])
        ans.append(sublist)
        ans.append([[nums[0]] + l for l in sublist])
        return sum(ans, [])

sol = Solution()
print(sol.subsets([0]))
print(sol.subsets([1,2,3]))
