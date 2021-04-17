from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # use a counter to compare strings between s and p
        # O(n) time, O(1) space
        
        def strToCount(s_str: str) -> List[int]:
            """convert a string into letter counts"""
            s_count = [0] * 26
            for c in s_str:
                s_count[ord(c) - ord('a')] += 1
            return s_count
        
        p_count = strToCount(p)
        curr_s = strToCount(s[:len(p)])
        ans = []
        if p_count == curr_s:
            ans = [0]
        for idx in range(0, len(s) - len(p)):
            curr_s[ord(s[idx]) - ord('a')] -= 1
            curr_s[ord(s[idx + len(p)]) - ord('a')] += 1
            if p_count == curr_s:
                ans.append(idx+1)
        return ans

sol = Solution()
print(sol.findAnagrams("cbaebabacd", "bac"))
