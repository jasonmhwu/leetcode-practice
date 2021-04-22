from typing import List
from collections import Counter
from itertools import accumulate


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # record the brick boundaries of each row in a counter
        # find the boundary that has max count
        # O(N) time, O(N) space, N is the number of bricks
        count = Counter()
        for row in wall:
            count.update(list(accumulate(row[:-1])))
        return len(wall) - (max(count.values()) if count else 0)

sol = Solution()
print(sol.leastBricks([[1], [1]]))
