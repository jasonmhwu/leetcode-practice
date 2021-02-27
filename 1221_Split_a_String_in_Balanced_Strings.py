from collections import deque


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = deque()
        ans = 0
        for c in s:
            if not stack or c == stack[-1]:
                stack.append(c)
            else:
                stack.pop()
                if not stack:
                    ans += 1
        return ans

sol = Solution()
print(sol.balancedStringSplit("RLRRLLRLRL"))
