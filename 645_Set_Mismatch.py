from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # length = len(nums)
        # find missing num -> sum_to_n - sum(set(nums))
        # find repeat num -> sum((nums)) + missing_num - sum_to_n
        # takes O(n) time, O(n) space
        
        length = len(nums)
        sum_to_n = (length+1) * length // 2
        
        missing_num = sum_to_n - sum(set(nums))
        repeat_num = sum(nums) + missing_num - sum_to_n
        
        return [repeat_num, missing_num]
