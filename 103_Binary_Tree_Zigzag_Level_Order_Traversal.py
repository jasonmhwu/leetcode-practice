from collections import deque
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        # typical BFS, but return alternating order
        # O(n) time, O(logn) space
        if not root:
            return [] 
        queue, ans, left2right = deque([root]), [], True
        while queue:
            values = []
            len_queue = len(queue)
            for _ in range(len_queue):
                node = queue.popleft()
                values.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if left2right:
                ans.append(values)
            else:
                ans.append(values[::-1])
            left2right = not left2right
        return ans
