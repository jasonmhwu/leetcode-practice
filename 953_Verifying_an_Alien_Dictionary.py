import string
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # approach 1: replace each character with uppercase original alphabet
        # 'hello' -> 'AGBBO'
        # check whether the list is in sorted order
        # O(NK) time, O(NK) space
        
        for alien, orig in zip(order, string.ascii_uppercase):
            for idx, w in enumerate(words):
                words[idx] = w.replace(alien, orig)
        for i in range(len(words)-1):
            if words[i] > words[i+1]:
                return False
        return True
        
