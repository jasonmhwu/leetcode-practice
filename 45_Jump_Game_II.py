from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # dynamic programming:
        # dp[i]: minimum number of jumps to reach index i
        # for each i, dp[i+1:i+nums[i]] = min(original,  dp[i]+1)
        # if reaching the end, stop
        # O(n) time, O(n) space
        dp = [10**6] * len(nums)
        visited = [False] * len(nums)
        visited[0] = True
        dp[0] = 0
        
        for i in range(len(nums)):
            for j in range(i+1, min(i+nums[i]+1, len(nums))):
                if visited[j]:
                    continue
                dp[j] = dp[i] + 1
                visited[j] = True
                if j == len(nums) - 1:
                    return dp[-1]
        return dp[-1]
        
sol = Solution()
print(sol.jump([2,3,1,1,4]))
