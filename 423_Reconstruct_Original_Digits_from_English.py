from collections import Counter


class Solution:
    def __init__(self):
        self.digit2counter = {
            0: Counter('zero'),
            1: Counter('one'),
            2: Counter('two'),
            3: Counter('three'),
            4: Counter('four'),
            5: Counter('five'),
            6: Counter('six'),
            7: Counter('seven'),
            8: Counter('eight'),
            9: Counter('nine')
        }
        self.order = (0, 2, 4, 6, 8, 5, 3, 7, 1, 9)
        
    def originalDigits(self, s: str) -> str:
        # idea: transform string s and all digit words into counter
        # O(n) time to construct s_counter, O(1) memory space
        
        digit_count = [0] * 10
        s_counter = Counter(s)
        
        for d in self.order:
            count_d = min([s_counter[c] for c in self.digit2counter[d].keys()])
            digit_count[d] = count_d
            for c in self.digit2counter[d].keys():
                s_counter[c] -= count_d
        
        ans_string = ''
        for i in range(10):
            ans_string += str(i) * digit_count[i]
        return ans_string

sol = Solution()
print(sol.originalDigits("zerotwofiveseven"))
