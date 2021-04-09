class Trie:
    # each character is a 26-row dictionary: 'a' -> dict(other characters after 'a')
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._trie = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr_dict = self._trie
        for w in word:
            if w not in curr_dict.keys():
                curr_dict[w] = dict()
            curr_dict = curr_dict[w]
        curr_dict['EOW'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr_dict = self._trie
        for w in word:
            if w not in curr_dict.keys():
                return False
            curr_dict = curr_dict[w]
        if 'EOW' in curr_dict.keys():
            return True
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr_dict = self._trie
        for w in prefix:
            if w not in curr_dict.keys():
                return False
            curr_dict = curr_dict[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
