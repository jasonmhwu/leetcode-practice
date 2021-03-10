from typing import List


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        # dp[i] = minimum height when bookshelf contains book[:(i+1)]
        # dp[i] = min(dp[i-j]  +  max(books[i-j+1][1] ~ books[i][1]))  j = 1 ~ sum(books) >= width
        dp = [0] * len(books)
        dp[0] = books[0][1]
        for i in range(1, len(books)):
            min_height = 10**6
            j = 1
            sum_width = books[i][0]
            curr_height = books[i][1]
            while sum_width <= shelf_width:
                if dp[i-j] + curr_height < min_height:
                    min_height = dp[i-j] + curr_height
                j += 1
                sum_width += books[i-j+1][0]
                curr_height = max(books[i-j+1][1], curr_height)
            dp[i] = min_height
        return dp[-1]

sol = Solution()
print(sol.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4))
