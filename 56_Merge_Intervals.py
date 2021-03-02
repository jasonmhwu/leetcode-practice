from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # first sorted by start
        # use a stack to store intervals
        
        intervals = sorted(intervals, key=lambda x: x[0])
        stack = []
        for i in intervals:
            if not stack or i[0] > stack[-1][1]:
                stack.append(i)
            else:
                prev_i = stack.pop()
                stack.append([prev_i[0], max(prev_i[1], i[1])])
        return stack

sol = Solution()
print(sol.merge([[1,4], [4,5]]))
print(sol.merge([[1,4]]))
print(sol.merge([[1,4], [2,3]]))
