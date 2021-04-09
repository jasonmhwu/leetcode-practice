from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # approach 1: sort nums, and sweep nums to find longest sequence
        # O(nlogn) time, O(n) space
        # approach 2: keep all current consecutive sequences in a set
        # for each new number, find neighbors (1 - 2), connect new sequence and add back to set
        # O(n) time, O(n) space
        if not nums:
            return 0
        nums = set(nums)
        curr_seq = dict()
        max_length = 1 
        for n in nums:
            curr_seq[n] = [n]
            if n+1 in curr_seq.keys():
                seq = curr_seq.pop(n+1)
                curr_seq[n] = curr_seq[n] + seq
                curr_seq[seq[-1]] = curr_seq[n]
                max_length = max(max_length, len(curr_seq[n]))
            if n-1 in curr_seq.keys():
                seq = curr_seq.pop(n-1)
                new_seq = seq + curr_seq[n]
                curr_seq[new_seq[-1]] = new_seq
                curr_seq[new_seq[0]] = new_seq
                max_length = max(max_length, len(new_seq))
        return max_length

sol = Solution()
print(sol.longestConsecutive([]))
print(sol.longestConsecutive([2]))
print(sol.longestConsecutive([100,4,200,1,3,2]))
