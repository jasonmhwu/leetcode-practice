class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # determine length + the k-th node before the end
        # at most 2-pass, O(n) time, O(1) space
        if not head:
            return 
        if k == 0:
            return head
        length, dummy_head = 0, ListNode(0, head)
        old_ptr, new_ptr = dummy_head, dummy_head
        while old_ptr and old_ptr.next:
            if length >= k:
                new_ptr = new_ptr.next
            old_ptr = old_ptr.next
            length += 1
        
        if length <= k:
            return self.rotateRight(head, k%length)
        else:
            old_ptr.next = head
            new_head = new_ptr.next
            new_ptr.next = None
            return new_head


