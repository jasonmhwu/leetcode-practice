class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n**2) time, 
        # use each index or index pair as starting point, O(n) operations to find longest substring
        ans = s[0]
        for start in range(len(s)):
            for end in range(start, start+2):
                if end > len(s)-1 or s[start] != s[end]:
                    continue
                j = 1
                while start-j >= 0 and end+j < len(s) and s[start-j] == s[end+j]:
                    j += 1
                if 2*j -1 + end - start > len(ans):
                    ans = s[start-j+1:end+j]
        return ans

sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))
