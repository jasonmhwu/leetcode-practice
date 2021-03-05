# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # get length of the linked list
        # reverse the linked list till middle
        # start from middle nodes and traverse toward the ends
        # O(n) time, O(1) space
        # I can optimize this
        length = 0
        ptr = head
        while ptr:
            length += 1
            ptr = ptr.next
        
        ptr = head
        future_ptr = head.next
        ptr.next = None
        for _ in range((length+1)//2 - 1):
            next_node = future_ptr
            future_ptr = next_node.next
            next_node.next = ptr
            ptr = next_node
        
        if length % 2:
            ptr_forward, ptr_reverse = ptr, ListNode(ptr.val, future_ptr)
        else:
            ptr_forward, ptr_reverse = ptr, future_ptr
        while ptr_forward and ptr_reverse:
            if ptr_forward.val != ptr_reverse.val:
                return False
            ptr_forward, ptr_reverse = ptr_forward.next, ptr_reverse.next
        return True
