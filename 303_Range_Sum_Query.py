from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            self.cum_sum = []
        else:
            self.cum_sum = [nums[0]]
            for n in nums[1:]:
                self.cum_sum.append(self.cum_sum[-1] + n)

    def sumRange(self, i: int, j: int) -> int:
        if not self.cum_sum:
            return 0
        if i == 0:
            return self.cum_sum[j]
        else:
            return self.cum_sum[j] - self.cum_sum[i-1]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
