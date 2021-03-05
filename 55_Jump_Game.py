from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # use stack to store reachable indices
        # for each step, pop the last index and extend with new reachable index
        # TLE
        
        # solution 2:
        # use a range to record reachable index
        # O(n) time, O(1) space
        if nums[0] == 0:
            return True if len(nums) == 1 else False
        reachable = [0, nums[0]]
        while reachable[0] <=  reachable[1]:
            if reachable[1] >= len(nums)-1:
                return True
            new_max = reachable[0] + nums[reachable[0]]
            if new_max > reachable[1]:
                reachable[1] = new_max
            reachable[0] += 1
        return False

sol = Solution()
print(sol.canJump([2,3,1,1,4]))
print(sol.canJump([3,2,1,0,4]))
