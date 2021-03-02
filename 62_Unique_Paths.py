class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # use DP to solve this problem, should take O(m*n) time and O(n) space
        # theoretically can reduce down to O(min(m, n)) space by doing column-based
        
        ctr = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                ctr[j] += ctr[j-1]
        return ctr[-1]

sol = Solution()
print(sol.uniquePaths(3, 7))
