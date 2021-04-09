class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # O(n) time, O(1) space
        if not l1:
            return l2
        if not l2:
            return l1
        
        ptr1, ptr2 = l1, l2
        ans = curr_node = ListNode(-101)
        while ptr1 and ptr2:
            if ptr1.val <= ptr2.val:
                curr_node.next = ptr1
                curr_node = curr_node.next
                ptr1 = ptr1.next
            else:
                curr_node.next = ptr2
                curr_node = curr_node.next
                ptr2 = ptr2.next
        curr_node.next = ptr2 if not ptr1 else ptr1
        return ans.next


