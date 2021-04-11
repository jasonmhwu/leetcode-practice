class Solution:
    def isHappy(self, n: int) -> bool:
        # keep applying the process and record results
        # if results == 1, return True
        # if results are seen before, return False
        # O(logn) time, O(n) space
        observed = set([n])
        while True:
            n = sum([int(d)**2 for d in str(n)])
            if n == 1:
                return True
            if n in observed:
                return False
            observed.add(n)

sol = Solution()
print(sol.isHappy(1))
print(sol.isHappy(19))
