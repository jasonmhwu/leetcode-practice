from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # use a list to store the answer
        # sort people according to the height: O(nlogn) time
        # for each, starting from the highest, insert(k_i, entry): O(n**2) time
        # takes O(n**2) time, O(n) space
        people_sorted = sorted(people, key=lambda x: (-x[0], x[1]))
        ans = []
        for p in people_sorted:
            ans.insert(p[1], p)
        return ans

sol = Solution()
print(sol.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))
