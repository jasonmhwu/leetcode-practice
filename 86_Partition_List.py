class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        # create a dummy node and apppend all nodes >= x behind it
        # append new  list at the end of old list
        # O(n) time, O(1) space
        if not head:
            return None
        dummy = curr_larger = ListNode(-1000)
        dummy_head = ListNode(-1000, next=head)
        
        curr_ptr = dummy_head
        while curr_ptr and curr_ptr.next:
            if curr_ptr.next.val >= x:
                curr_larger.next = curr_ptr.next
                curr_larger = curr_larger.next
                curr_ptr.next = curr_ptr.next.next
            else:
                curr_ptr = curr_ptr.next
        curr_larger.next = None
        curr_ptr.next = dummy.next
        return dummy_head.next
