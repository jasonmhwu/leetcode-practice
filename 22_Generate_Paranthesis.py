from typing import List


class Solution:
    def __init__(self):
        self._memo = {1: set(["()"])}
        self._maxn = 1
        
    def generateParenthesis(self, n: int) -> List[str]:
        # for each clause from n-1, insert paranthesis at each possible location
        while n > self._maxn:
            new_set = []
            for clause in self._memo[self._maxn]:
                new_set.extend([[clause[:idx]+'()'+clause[idx:]] for idx in range(len(clause))])
            self._memo[self._maxn + 1] = set(sum(new_set, []))
            self._maxn += 1
        return self._memo[n]

sol = Solution()
print(sol.generateParenthesis(4))
