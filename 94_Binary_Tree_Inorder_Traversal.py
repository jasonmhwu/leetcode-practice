# Definition for a binary tree node.
from typing import List

OFFSET = 300

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # recursive solution
        # O(n) time, O(n) space
        
        #if not root:
        #    return []
        #return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    
        # iterative solution
        # use a stack to store right, root, left node
        # add to ans if node is  leaf
        # O(n) time, O(n) space
        if not root:
            return []
        ans = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node.val > 100:
                ans.append(node.val - OFFSET)
            else:
                if node.right:
                    stack.append(node.right)
                stack.append(TreeNode(node.val + OFFSET))
                if node.left:
                    stack.append(node.left)
        return ans
                    
