# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        # O(N) time
        
        length = 0
        ptr = head
        while ptr:
            length += 1
            ptr = ptr.next
        
        ptr1, ptr2 = head, head
        for _ in range(k-1):
            ptr1 = ptr1.next
        for _ in range(length-k):
            ptr2 = ptr2.next
        ptr1.val, ptr2.val = ptr2.val, ptr1.val
        return head
        
