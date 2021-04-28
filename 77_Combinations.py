from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n == k:
            return [list(range(1, n+1))]
        if  k == 1:
            return [[i] for i in range(1, n+1)]
        ans = [comb + [n] for comb in self.combine(n-1, k-1)] + self.combine(n-1, k)
        return ans

sol = Solution()
print(sol.combine(4, 2))
