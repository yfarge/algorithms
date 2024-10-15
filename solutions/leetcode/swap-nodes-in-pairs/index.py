from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode(-1)
        dummy.next = head
        while head and head.next:
            n1 = head
            n2 = head.next
            n1.next = n2.next
            n2.next = n1
            prev.next = n2
            prev = n1
            head = head.next

        return dummy.next
