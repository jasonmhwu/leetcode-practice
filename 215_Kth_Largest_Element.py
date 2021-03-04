from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # brute force: call sorting algorithm, and the pick the kth element. O(nlogn) time
        # nums_sorted = sorted(nums, reverse=True)
        # return nums_sorted[k-1]

        # use priority queue: takes O(n) to form the heap
        # takes O(klogn) time to pop k elements
        # heapq.heapify(nums)
        # for _ in range(len(nums)-k+1):
        #     ans = heapq.heappop(nums)
        # return ans
    
        # use Quick-select: should take O(n) time
        if not nums:
            return -1
        
        pivot = nums[0]
        left = [x for x in nums if x > pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x < pivot]
        
        if len(left) >= k:
            return self.findKthLargest(left, k)
        elif len(left) + len(mid) < k:
            return self.findKthLargest(right, k-len(left)-len(mid))
        else:
            return mid[0]

sol = Solution()
print(sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4))
