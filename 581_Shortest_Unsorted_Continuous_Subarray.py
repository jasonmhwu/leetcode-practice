from typing import List

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # motivation: if sees decreasing numbers, both ends should be in the subarray
        # need to keep track of the min and max number in the subarray
        # O(n) time, O(1) space

        
        l, r = -1, 0
        min_elm, max_elm = 10 ** 5, -10**5
        
        # find all decreasing neighboring numbers
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                if l < 0:
                    l = i-1
                r = i
        
        # array is sorted       
        if l < 0:
            return 0
        
        min_elm = min(nums[l:r+1])
        max_elm = max(nums[l:r+1])
        # find the left elements bigger than min_elm
        for i in range(l):
            if nums[i] > min_elm:
                l = i
                break
        # find the right elements smaller than max_elm
        for i in range(r+1, len(nums)):
            if nums[i] < max_elm:
                r = i

        return r - l + 1

sol = Solution()
print(sol.findUnsortedSubarray([2,6,4,8,10,9,15]))
