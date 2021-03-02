from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # takes O(n!) space, O(n!) time
        # write a recursive formula
        if len(nums) <= 1:
            return [nums]
        
        ans = []
        for i in range(len(nums)):
            ans.append([[nums[i]] + res for res in self.permute(nums[:i] + nums[i+1:])])
        return sum(ans, [])

sol = Solution()
print(sol.permute([1]))
print(sol.permute([0, 1]))
print(sol.permute([1, 2, 3]))
