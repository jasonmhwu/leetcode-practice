class Solution:
    def minOperations(self, n: int) -> int:
        # odd n: ans = ((n**2)-1) / 4
        # even n: ans = n**2 / 4
        return int((n*n - (n%2)) / 4)

sol = Solution()
print(sol.minOperations(1))
print(sol.minOperations(2))
print(sol.minOperations(3))
print(sol.minOperations(10))
