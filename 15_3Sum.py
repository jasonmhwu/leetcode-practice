from collections import Counter, defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_counter = Counter(nums)
        nums = sum([[n] * min(count, 3) for n, count in nums_counter.items()], [])
        nums.sort()
        
        ans = []
        for i in range(len(nums) - 2):
            if (i > 0) and (nums[i] == nums[i-1]):
                continue
            
            left, right = i+1, len(nums)-1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if curr_sum > 0:
                    right -= 1
                elif curr_sum < 0:
                    left += 1
                else:
                    ans.append([nums[i],  nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while (left < len(nums)) and (nums[left-1] == nums[left]):
                        left += 1
                    while (right > 0) and (nums[right+1] == nums[right]):
                        right -= 1
        return ans
