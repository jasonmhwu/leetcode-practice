from collections import Counter
from typing import List


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        # brute force: compares a to b take O(nlogn) time, overall takes O(A*B*nlogn)
        # don't sort a and b, use a Counter ->  overall time to O(A*B*n)
        # calculate the max count for each character in B, compare each a to B, overall time O(max(A, B)*n)
        
        def isSubset(a, b) -> bool:
            """return whether b is a subset of a."""
            for c, c_count in b.items():
                if c_count > a[c]:
                    return False
            return True
        
        max_ctr_B = Counter("")
        for b in B:
            for c, c_count in Counter(b).items():
                max_ctr_B[c] = max(max_ctr_B[c], c_count)
        
        ans = []
        for a in A:
            if isSubset(Counter(a), max_ctr_B):
                ans.append(a)
        return ans
