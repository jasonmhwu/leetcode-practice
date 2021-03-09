from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        # use a queue to find all nodes at d-1, then add node
        if d == 1:
            return TreeNode(v, left=root)
        
        queue = deque([root])
        curr_depth = 1
        while curr_depth < d-1:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            curr_depth += 1
        
        # add new nodes
        for node in queue:
            node.left = TreeNode(v, left=node.left)
            node.right = TreeNode(v, right=node.right)
        return root
