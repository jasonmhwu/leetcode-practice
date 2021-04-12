from typing import List


class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # start to create abs(a_i - a_j) == n-1
        # decrease until k distinct numbers  are  found
        # maintain difference till the end
        # target diff: n - k
        # O(n) time, O(1) space
        ans = [1] * n
        is_increasing = 1
        diff = n - 1
        for i in range(1, n):
            if diff > n - k:
                ans[i] = ans[i-1] + is_increasing * diff
                is_increasing *= -1
                diff -= 1
            else:
                ans[i] = ans[i-1] + is_increasing
        return ans

sol = Solution()
print(sol.constructArray(9, 2))
