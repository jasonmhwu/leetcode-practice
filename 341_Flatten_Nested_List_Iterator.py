# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._list = []
        self._idx = 0
        stack = nestedList[::-1]
        while stack:
            curr_list = stack.pop()
            if curr_list.isInteger():
                self._list.append(curr_list.getInteger())
            else:
                stack.extend(curr_list.getList()[::-1])
    
    def next(self) -> int:
        if self.hasNext():
            self._idx += 1
            return self._list[self._idx - 1]
    
    def hasNext(self) -> bool:
        return self._idx < len(self._list)

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
