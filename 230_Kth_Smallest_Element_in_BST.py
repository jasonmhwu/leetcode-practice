# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self._ctr = 0
        
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        # recursively traverse the tree using in-order traversal (left -> root -> right)
        # keep a negative counter, once the counter touches k return the number, else return -counter
        if not root:
            return -1
        
        if (ans := self.kthSmallest(root.left, k)) >= 0:
            return ans
        else:
            self._ctr += 1
            if self._ctr == k:
                self._ctr = 0
                return root.val
            else:
                return self.kthSmallest(root.right, k)

