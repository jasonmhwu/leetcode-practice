# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        # always merge into node of tree 1
        # use dfs to solve problem, takes O(n) time, O(n) space
        if not (root1 or root2):
            return None
        elif root1 and root2:
            root1.val += root2.val
            root1.left = self.mergeTrees(root1.left, root2.left)
            root1.right = self.mergeTrees(root1.right, root2.right)
            return root1
        elif root1:
            return root1
        elif root2:
            return root2
        else:
            pass

sol = Solution()
print(sol.mergeTrees(TreeNode(1, left=TreeNode(2)), None))        
