from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # recursive solution
        def helper(k: int, n: int, max_num: int) -> List[List[int]]:
            """return answers that use numbers from 1 to max_num"""
            #print(k, n, max_num)
            if k == 1:
                return [[n]] if 1 <= n <= max_num else []
            ans = []
            for largest in range(k, 1 + min(max_num, n-k*(k-1)//2)):
                ans.extend([comb + [largest] for comb in helper(k-1, n-largest, largest-1)])
            return ans
        
        return helper(k, n, 9)

sol = Solution()
print(sol.combinationSum3(9, 45))
