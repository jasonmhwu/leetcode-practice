from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # recursive solution
        # O(n) time and space
        '''
        if not root:
            return []
        else:
            return [root.val] + sum([self.preorder(c) for c in root.children], [])
        '''
        # iterative solution
        # O(n) time and space
        if not root:
            return []
        stack, ans = [root], []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            stack.extend(node.children[::-1])
        return ans

