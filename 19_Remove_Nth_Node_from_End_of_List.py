class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # use a two pointer
        # O(n) time, O(1) space
        dummy_head = ListNode(0, head)
        ptr_tail, ptr_head = dummy_head, dummy_head
        for _ in range(n):
            ptr_tail = ptr_tail.next
        while ptr_tail and ptr_tail.next:
            ptr_head = ptr_head.next
            ptr_tail = ptr_tail.next
        ptr_head.next = ptr_head.next.next
        return dummy_head.next

sol = Solution()
print(sol.removeNthFromEnd(ListNode(0), 1))
