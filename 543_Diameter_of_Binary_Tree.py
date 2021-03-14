# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0
        
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # do dfs in the order of left, right, root
        # mark each node
        
        def dfs(root):
            if not root:
                return 0
            left_depth, right_depth = dfs(root.left), dfs(root.right)
            if left_depth + right_depth > self.diameter:
                self.diameter = left_depth + right_depth
            return max(left_depth, right_depth) + 1
        
        dfs(root)
        return self.diameter
