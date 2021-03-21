class Solution:
    def __init__(self):
        self.power_set = set()
        self.create_power_set()
        
    def create_power_set(self):
        """create a set of all power of 2 numbers stored as sorted digit string."""
        num = 1
        while num < 10**9:
            self.power_set.add(self.numToSortedString(num))
            num *= 2
    
    def numToSortedString(self, N: int):
        return ''.join(sorted(str(N)))
    
    def reorderedPowerOf2(self, N: int) -> bool:
        # 
        # each query takes O(log n) time
        return self.numToSortedString(N) in self.power_set

sol = Solution()
print(sol.reorderedPowerOf2(8042))
print(sol.reorderedPowerOf2(1))
