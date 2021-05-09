class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # approach 1: BFS (TLE)
        # if char is unique to one string -> delete
        # if I see two char that are different:
        # can delete either one (delete both is considered in later cases)
        """
        ans = 0
        ans_found = False
        min_operations = 10**5
        queue = deque([(word1, word2)])
        while queue:
            len_queue = len(queue)
            for _ in range(len_queue):
                w1, w2 = queue.popleft()
                idx = 0
                while idx < min(len(w1), len(w2)) and w1[idx] == w2[idx]:
                    idx += 1
                    continue
                if idx == len(w1):
                    ans_found = True
                    min_operations = min(min_operations, ans + len(w2) - idx)
                elif idx == len(w2):
                    ans_found = True
                    min_operations = min(min_operations, ans + len(w1) - idx)
                else:
                    queue.extend([(w1[idx+1:], w2[idx:]), (w1[idx:], w2[idx+1:])])
            ans += 1
            if ans_found and ans >= min_operations:
                return min_operations
        """
        # approach 2: 2-D dp
        # dp[i][j] = min delete operations on w1[i:] and w2[j:]
        # if w1[i] == w2[j]:
        # dp[i][j] == dp[i+1][j+1]
        # else:
        # dp[i][j] = 1 + (dp[i+1][j], dp[i][j+1])
        # O(MN) time, O(min(M, N)) space
        if len(word1) > len(word2):
            word1, word2 = word2, word1
        dp_prev = list(range(len(word1)+1)[::-1])
        for w2_idx in range(len(word2))[::-1]:
            dp_curr = [len(word2)-w2_idx] * (len(word1)+1)
            for w1_idx in range(len(word1))[::-1]:
                if word1[w1_idx] == word2[w2_idx]:
                    dp_curr[w1_idx] = dp_prev[w1_idx+1]
                else:
                    dp_curr[w1_idx] = 1 + min(dp_curr[w1_idx+1], dp_prev[w1_idx])
            dp_prev = dp_curr
        return dp_curr[0]

sol = Solution()
print(sol.minDistance("leetcode", "etco"))
