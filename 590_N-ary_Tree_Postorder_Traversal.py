from typing import  List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # recursive solution: O(n) time, O(n) space
        '''
        if not root:
            return []
        ans = []
        for child in root.children:
            ans += self.postorder(child)
        ans += [root.val]
        return ans
        '''
        
        # iterative solution:
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            if isinstance(node, int):
                ans.append(node)
                continue
            else:
                stack.append(node.val)
                for child in node.children[::-1]:
                    stack.append(child)
        return ans
        
        
