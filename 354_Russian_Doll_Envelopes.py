from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # dp approach
        # first sort envelopes using width and heights
        # dp[i]: maximum number of envelopes under envelope i
        # dp[i] = dp[j] + 1 if envelope j smaller than i
        # O(n**2) time, O(n) space
        # optimize: can I do O(nlogn) time
        envelopes = sorted(envelopes, key=lambda x: (x[0], x[1]))
        dp = [1] * len(envelopes)
        for i in range(1, len(dp)):
            for j in range(i)[::-1]:
                if dp[j] >= dp[i]-1 \
                    and envelopes[i][0] > envelopes[j][0] \
                    and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = dp[j] + 1
        return max(dp)

sol = Solution()
print(sol.maxEnvelopes([[1,1],[1,1],[1,1]]))
print(sol.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
