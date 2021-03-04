# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # step 1: walk through head A, change val to -val
        # step 2: walk through head B, if see negative value, then this is the intersection
        # step 3: walk through head A, change values back
        # O(n) time, O(1) space
        
        def reverseListValue(root):
            """change all values in the list to negative."""
            ptrA = root
            while ptrA:
                ptrA.val *= -1
                ptrA = ptrA.next

        if not (headA and headB):
            return None
        
        reverseListValue(headA)
        
        ptrB = headB
        while ptrB:
            if ptrB.val < 0: # found intersection
                reverseListValue(headA)
                return ptrB
            ptrB = ptrB.next
        reverseListValue(headA)
        return None

