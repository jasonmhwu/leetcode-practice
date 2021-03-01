from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        idx = 0
        for idx in range(len(nums)):
            while nums[idx] > 0:
                if nums[idx] == idx + 1:
                    nums[idx] = -1
                    continue
                if nums[nums[idx]-1] > 0:
                    tmp = nums[nums[idx]-1]
                    nums[nums[idx]-1] = -1
                    nums[idx] = tmp
                else:
                    break
            idx += 1
        return [i+1 for i in range(len(nums)) if nums[i] > 0]

sol = Solution()
print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))
print(sol.findDisappearedNumbers([1,1,1]))
print(sol.findDisappearedNumbers([3,3,3]))
print(sol.findDisappearedNumbers([1,2,3]))
