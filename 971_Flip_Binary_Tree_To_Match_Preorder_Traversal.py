from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        # use an iterative solution
        # idea: if the left node doesn't have the right value, swap left and right branches
        stack = [root]
        curr_idx = 0
        ans = []
        
        while stack:
            curr_node = stack.pop()
            if not curr_node:
                continue
            if curr_node.val == voyage[curr_idx]:
                if curr_node.left\
                    and curr_idx < len(voyage) - 1\
                    and curr_node.left.val != voyage[curr_idx + 1]:
                    curr_node.left, curr_node.right = curr_node.right, curr_node.left
                    ans.append(curr_node.val)
                    
                stack.append(curr_node.right)
                stack.append(curr_node.left)
                curr_idx += 1

            else:
                return [-1]
        return ans
        
