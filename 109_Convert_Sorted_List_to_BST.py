class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        # median node is always at the root
        # need to first find the median node
        # O(n) time and space
        def createTree(head: ListNode, length: int) -> TreeNode:
            """assign median node as root, and recursively build subtrees"""
            if length == 0:
                return None
            if length == 1:
                return TreeNode(head.val)
            median_idx = length // 2
            ptr = head
            for _ in range(median_idx):
                ptr = ptr.next
            return TreeNode(
                ptr.val,
                left=createTree(head, median_idx),
                right=createTree(ptr.next, length - median_idx - 1)
            )
        ptr = ListNode(0, head)
        length = 0
        while ptr.next:
            ptr = ptr.next
            length += 1
        return createTree(head, length)

