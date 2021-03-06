from typing import List


class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        # if one word is the sub-end of another, it doesn't need to be considered
        # sort on key=s[::-1]
        words = sorted(words, key=lambda w: w[::-1])
        ans = len(words[-1]) + 1
        for idx in range(len(words)-1):
            if words[idx] != words[idx+1][-len(words[idx]):]:
                ans += len(words[idx]) + 1
        return ans

sol = Solution()
print(sol.minimumLengthEncoding(["time", "me", "bell", "stime"]))
