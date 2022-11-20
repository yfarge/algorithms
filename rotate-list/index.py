# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        cur.next = head

        for _ in range(n - k % n):
            cur = cur.next
        new_head = cur.next
        cur.next = None

        return new_head
