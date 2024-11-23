from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = f = head

        while f and f.next:
            s = s.next
            f = f.next.next

        dummy = s.next
        p = s.next = None
        while dummy:
            n = dummy.next
            dummy.next = p
            p = dummy
            dummy = n

        l, r = head, p
        while r:
            n1, n2 = l.next, r.next
            l.next = r
            r.next = n1
            l, r = n1, n2
