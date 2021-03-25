class Solution:
    def countSubstrings(self, s: str) -> int:
        # brute force solution: check each start and end point, O(n**3) time
        # dp approach:
        # dp_prev: list of starting substrings that end in the previous character
        # dp_curr contains start if start+1 in dp_prev
        # O(n**2) time
        # O(n) space
        dp_prev = [0]
        dp_curr = []
        ans = 1
        
        for i in range(1, len(s)):
            dp_curr.append(i)
            if s[i-1] == s[i]:
                dp_curr.append(i-1)
            for start in dp_prev:
                if (start > 0) and s[start-1] == s[i]:
                    dp_curr.append(start-1)
            ans += len(dp_curr)
            dp_prev = dp_curr
            dp_curr = []
        return ans

sol = Solution()
print(sol.countSubstrings("aaa"))
print(sol.countSubstrings("a"))
print(sol.countSubstrings("aaabaaa"))
