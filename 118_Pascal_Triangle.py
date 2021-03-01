from typing import List


class Solution:
    def __init__(self):
        self._memo = {1: [1]}
        self.max_rows = 1
        
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows > self.max_rows:
            for i in range(self.max_rows, numRows):
                prev_array = self._memo[i]
                new_array = [sum(prev_array[(n-1):(n+1)]) for n in range(1, len(prev_array)+1)]
                new_array.insert(0, 1)
                self._memo[i+1] = new_array
            self.max_rows = numRows
        return [self._memo[i] for i in range(1, numRows+1)]

sol = Solution()
print(sol.generate(5))
