from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        # create a tmp_code that repeats code twice
        # start with tmp_code[n]
        # use a single list to add up numbers
        # takes O(n*k) time, O(n) space
        n = len(code)
        if k == 0:
            return [0] * n
        
        tmp_code = code + code
        if k > 0:
            return [sum(tmp_code[i+1:i+k+1]) for i in range(n)]
        else:
            return [sum(tmp_code[i+k:i]) for i in range(n, 2*n)]

sol = Solution()
print(sol.decrypt([5,7,1,4], 3))
print(sol.decrypt([5,7,1,4], 0))
print(sol.decrypt([5,7,1,4], -2))
