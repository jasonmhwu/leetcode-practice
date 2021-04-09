from collections import deque
from typing import List


class Solution:
    def __init__(self):
        self.digit2letter = {
            '2': ('a', 'b', 'c'),
            '3': ('d', 'e', 'f'),
            '4': ('g', 'h', 'i'),
            '5': ('j', 'k', 'l'),
            '6': ('m', 'n', 'o'),
            '7': ('p', 'q', 'r', 's'),
            '8': ('t', 'u', 'v'),
            '9': ('w', 'x', 'y', 'z')
        }
        
    def letterCombinations(self, digits: str) -> List[str]:
        # O(4 ** n) time, O(1) memory
        if not digits:
            return []
        ans = deque(self.digit2letter[digits[0]])
        for d in digits[1:]:
            curr_letter = self.digit2letter[d]
            len_ans = len(ans)
            for _ in range(len(ans)):
                curr_comb = ans.popleft()
                ans.extend([curr_comb + l for l in curr_letter])
        return ans

sol = Solution()
print(sol.letterCombinations("23"))

