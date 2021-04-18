class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.visited = dict()
        
    def rob(self, root: TreeNode) -> int:
        # go from leaf layer to head 
        # use BFS to record nodes in each layer
        # dp[node] = max(dp[left] + dp[right], val + dp[grandchildren])
        # utilize tree to directly store dp values
        # O(n) time, O(n) space for BFS 
        # iterative solution
        '''
        stack = [[root]]
        while stack[-1]:
            new_layer = []
            for node in stack[-1]:
                if node.left:
                    new_layer.append(node.left)
                if node.right:
                    new_layer.append(node.right)
            stack.append(new_layer)
        stack.pop()
        
        for l in range(len(stack))[::-1]:
            for node in stack[l]:
                val_prev_layer, val_curr_layer = 0, node.val
                if node.left:
                    val_prev_layer += node.left.val
                    val_curr_layer += (node.left.left.val if node.left.left else 0) +\
                                      (node.left.right.val if node.left.right else 0)
                if node.right:
                    val_prev_layer += node.right.val
                    val_curr_layer += (node.right.left.val if node.right.left else 0) +\
                                      (node.right.right.val if node.right.right else 0)
                node.val = max(val_prev_layer, val_curr_layer)
        return root.val
        '''
        # recursive solution
        # keep a visited dict to memoize visited nodes
        # O(n) time, O(n) space for stack
        if not root:
            return 0
        if root in self.visited.keys():
            return self.visited[root]
        curr_max = root.val
        if root.left:
            curr_max += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            curr_max += self.rob(root.right.left) + self.rob(root.right.right)
        self.visited[root] = max(curr_max, self.rob(root.left) + self.rob(root.right))
        return self.visited[root]


