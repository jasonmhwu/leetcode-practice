class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        # simple BFS approach
        # O(n) time, O(logn) space
        
        # basically binary search on the final layer
        # O(log n) nodes, needs O(log(logn)) search, each takes O(logn) steps
        # O(log(logn)*logn) time
        def existNode(idx) -> bool:
            '''check if node idx is in the tree.'''
            seq = bin(idx+1)[3:]
            node = root
            for i in seq:
                if i == '1':
                    node = node.right
                else:
                    node = node.left
            return True if node else False
            
        if not root:
            return 0
        node = root
        node_id = 0
        while node.left:
            node = node.left
            node_id = node_id*2 + 1
        left, right = node_id, node_id*2
        while left < right:
            mid = (left + right + 1) // 2
            if existNode(mid):
                left = mid
            else:
                right = mid - 1
        return left + 1
        
