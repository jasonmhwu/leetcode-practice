from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        # use a BFS (queue) to find the average for each level
        # takes O(n) time and O(n) space
        if not root:
            return []
        
        ans = [root.val]
        queue = collections.deque([root])
        while queue:
            length = len(queue)
            values = []
            for _ in range(length):
                n = queue.popleft()
                if n.left:
                    queue.append(n.left)
                    values.append(n.left.val)
                if n.right:
                    queue.append(n.right)
                    values.append(n.right.val)
            if values:
                ans.append(sum(values)/len(values))
        return ans
            
