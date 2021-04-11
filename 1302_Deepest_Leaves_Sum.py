from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        # use BFS, record the sum of values from the previous layer
        # O(n) time and space
        queue = deque([root])
        curr_sum = 0
        prev_layer_sum = root.val
        while queue:
            curr_sum = 0
            len_queue = len(queue)
            for _ in range(len_queue):
                node = queue.popleft()
                curr_sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            prev_layer_sum = curr_sum
        return prev_layer_sum


