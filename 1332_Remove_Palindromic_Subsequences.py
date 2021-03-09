class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # insight: answer is at most 2
        if not s:
            return 0
        elif s == s[::-1]:
            return 1
        else:
            return 2

sol = Solution()
print(sol.removePalindromeSub(""))
print(sol.removePalindromeSub("ababa"))
print(sol.removePalindromeSub("aaabbb"))
