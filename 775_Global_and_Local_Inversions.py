from typing import List


class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        # every local inversion is a global inversion
        # A is ideal permutation iff A is created by flipping neighboring elements
        # O(n) time,  O(1) space
        return all([abs(a - i) <= 1 for i, a in enumerate(A)])

sol = Solution()
print(sol.isIdealPermutation([0]))
print(sol.isIdealPermutation([1,0,2]))
print(sol.isIdealPermutation([1,2,0]))
