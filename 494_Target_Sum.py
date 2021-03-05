from math import comb
from typing import List
from collections import Counter


class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # brute force: try all combinations. O(2**n) time
        # idea1 : use a counter (pretty slow)
        # for each number, calculate all possible combinations from these numbers
        # if abs(rest of the nums summed) < remaining target, throw these away
        
        def helper(nums_dict, S):
            """takes in nums counter and target S, returns number of ways"""
            if not nums_dict:
                return 1 if S == 0 else 0
            
            num = max(nums_dict.keys())
            num_count = nums_dict.pop(num)
            remaining_sum = sum([k*v for k, v in nums_dict.items()])
            #print(nums_dict, remaining_sum, S)
            
            ans = 0
            num_sum = -num*num_count
            for i in range(num_count+1):
                if -remaining_sum <= S - num_sum <= remaining_sum:
                    ans += helper(nums_dict.copy(), S-num_sum) * comb(num_count, i)
                num_sum += 2*num
            return ans
                
        nums_dict = Counter(nums)
        return helper(nums_dict, S)

sol = Solution()
print(sol.findTargetSumWays([1,1,1,1,1], 3))
print(sol.findTargetSumWays([1,1,2,2,4,6], 10))
