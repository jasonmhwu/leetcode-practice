class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        # traverse the tree using dfs
        # for node i:
        # maxsum = max(maxsum, left + val + right)
        # return val + max(left, right)
        def traversal(node: TreeNode) -> int:
            """
            updates max sum with paths not involving parents,
            and returns max sum using node as intermediate point.
            """
            if not node:
                return 0
            left_path = traversal(node.left)
            right_path = traversal(node.right)
            maxsum[0] = max(
                maxsum[0],
                left_path if left_path > 0 else -2**31,
                right_path if right_path > 0 else -2**31,
                node.val,
                node.val + left_path + right_path
            )
            return node.val + max(left_path, right_path, 0)
        
        maxsum = [-2**31]
        through_root = traversal(root)
        return max(maxsum[0], through_root)
