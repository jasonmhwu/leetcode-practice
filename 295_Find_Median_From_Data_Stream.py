import heapq


class MedianFinder:
    # use two heap (smaller, larger) to keep values
    # find median -> O(1), get max from smaller heap and min from larger heap
    # addNum -> retrieve shorter heap, if num > min elm, move min elm to another heap and push num
    # O(1) time, O(n) space
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap_smaller, self.heap_larger = [], []
        heapq.heapify(self.heap_smaller)
        heapq.heapify(self.heap_larger)

    def addNum(self, num: int) -> None:
        if num >= self.findMedian():
            heapq.heappush(self.heap_larger, num)
        else:
            heapq.heappush(self.heap_smaller, -num)
        if len(self.heap_smaller) > len(self.heap_larger) + 1:
            heapq.heappush(self.heap_larger, -heapq.heappop(self.heap_smaller))
        if len(self.heap_larger) > len(self.heap_smaller) + 1:
            heapq.heappush(self.heap_smaller, -heapq.heappop(self.heap_larger))

    def findMedian(self) -> float:
        if not self.heap_smaller and not self.heap_larger:
            return 0
        elif len(self.heap_smaller) == len(self.heap_larger):
            return (self.heap_larger[0] - self.heap_smaller[0]) / 2
        elif len(self.heap_smaller) > len(self.heap_larger):
            return -self.heap_smaller[0]
        else:
            return self.heap_larger[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
