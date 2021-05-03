from typing import List


class WordFilter:
    # specify all possible prefix-suffix combination as keys and index as values
    # O(N*K**2) time for initialization, O(1) search
    # O(N*K**2) space
    def __init__(self, words: List[str]):
        self.searchdict = dict()
        for idx, w in enumerate(words):
            for pre_idx in range(1, 1+len(w)):
                for post_idx in range(1, 1+len(w)):
                    self.searchdict[w[:pre_idx] + '.' + w[-post_idx:]] = idx
        print(self.searchdict)

    def f(self, prefix: str, suffix: str) -> int:
        return self.searchdict.get(prefix + '.' + suffix, -1)

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
