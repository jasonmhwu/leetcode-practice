from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # starting from the largest candidate, use 1, 2, 3 or more instances and pass the remaining list down recursively
        
        if len(candidates) == 1:
            if target % candidates[0] == 0:
                return [[candidates[0]] * (target // candidates[0])]
            else:
                return []
        
        ans = []
        for i in range(target // candidates[0] + 1):
            if (res := self.combinationSum(candidates[1:], target - i*candidates[0])):
                ans.append([[candidates[0]] * i + n for n in res])
        return sum(ans, [])

sol = Solution()
print(sol.combinationSum([2,3,6,7], 7))
print(sol.combinationSum([1], 2))
print(sol.combinationSum([1], 1))
print(sol.combinationSum([2], 1))
