from typing import List
import heapq


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        # store negative target values in a min_heap
        # get largest target, replace it with target % other_sum or other_sum
        # keep track of sum
        # O(nlogn) time, O(n) space
        if len(target) == 1:
            return target == [1]
        curr_sum = sum(target)
        neg_target = [-n for n in target]
        heapq.heapify(neg_target)
        while curr_sum > len(target):
            largest_elm = -heapq.heappop(neg_target)
            other_sum = curr_sum - largest_elm
            if largest_elm <= other_sum:
                return False
            if largest_elm % other_sum == 0:
                heapq.heappush(neg_target, -other_sum)
                curr_sum = curr_sum - largest_elm + other_sum
            else:
                heapq.heappush(neg_target, -(largest_elm % other_sum))
                curr_sum = curr_sum - largest_elm + largest_elm % other_sum
        return True
            
sol = Solution()
print(sol.isPossible([3,5,9]))
print(sol.isPossible([2]))
