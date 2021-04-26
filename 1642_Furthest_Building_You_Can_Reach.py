import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        # BFS approach
        # at each building, take all viable options in the queue, move forward using bricks or ladders
        # O(2**H) time
        
        # use bricks first, and record number of bricks used in a heap
        # when run out of bricks, replace highest number of bricks with a ladder
        # O(HlogK) time, O(H) space
        brick_list = []
        heapq.heapify(brick_list)
        for idx in range(1, len(heights)):
            if (diff := heights[idx] - heights[idx-1]) > 0:
                heapq.heappush(brick_list, -diff)
                bricks -= diff
                while bricks < 0:
                    if ladders > 0:
                        ladders -= 1
                        bricks -= heapq.heappop(brick_list) if brick_list else 0
                    else:
                        return idx - 1
        return len(heights)-1
