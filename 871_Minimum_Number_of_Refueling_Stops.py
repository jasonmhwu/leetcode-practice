import heapq
from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # O(2**n) approach: roll out all possibilities
        # heap approach: O(nlogn) time, O(n) space
        idx = 0
        min_stops = 0
        stations.append([target, 0])
        gas_heap = []
        while idx < len(stations):
            if stations[idx][0] <= startFuel:
                heapq.heappush(gas_heap, -stations[idx][1])
                idx += 1
            else:
                if not gas_heap:
                    return -1
                else:
                    startFuel -= heapq.heappop(gas_heap)
                    min_stops += 1
        return min_stops


