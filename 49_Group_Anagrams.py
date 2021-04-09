import string
from collections import defaultdict, Counter
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(n) time, O(n) space
        count2word = defaultdict(list)
        for s in strs:
            s_count = Counter(s)
            s_key = tuple([s_count[l] for l in string.ascii_lowercase])
            count2word[s_key].append(s)
        ans = []
        for anagrams in count2word.values():
            ans.append(anagrams)
        return ans

sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
