from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s, f = head, head
        while f and f.next:
            f = f.next.next
            s = s.next
            if f == s:
                s = head
                while s != f:
                    s = s.next
                    f = f.next
                return s
        return None
