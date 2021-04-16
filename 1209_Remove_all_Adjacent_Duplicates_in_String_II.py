class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        # use character and counts like a stack to keep track of previous string
        # O(n) time, O(n) space
        stack = []
        for c in s:
            if not stack:
                stack.append([c, 1])
            elif c == stack[-1][0]:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
            if stack[-1][1] >= k:
                stack.pop()
        return ''.join([c[0] * c[1] for c in stack])

sol = Solution()
print(sol.removeDuplicates("deeedbbcccbdaa", 3))
