PRIME_NUM = 103

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # first thought: since keys and values are in a specific range, create a list for each key
        # second thought: we can use key % large prime number as the hash_key
        self.my_hash = [[]] * PRIME_NUM

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        tmp = self.my_hash[key % PRIME_NUM]
        if tmp and (idx := [idx for idx, (k, v) in enumerate(tmp) if k == key]):
            self.my_hash[key % PRIME_NUM][idx[0]] = (key, value)
        else:
            self.my_hash[key % PRIME_NUM].append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        tmp = self.my_hash[key % PRIME_NUM]
        if tmp and (v := [v for k, v in tmp if k == key]):
            return v[0]
        else:
            return -1
        
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        tmp = self.my_hash[key % PRIME_NUM]
        if tmp and (pair := [(k, v) for k, v in tmp if k == key]):
            self.my_hash[key % PRIME_NUM].remove(pair[0])

            


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1,2)
param_2 = obj.get(1)
obj.remove(1)
