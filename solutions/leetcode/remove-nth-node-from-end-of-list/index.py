from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        length = 0
        while dummy:
            length += 1
            dummy = dummy.next

        start = length - n
        dummy = head
        prev = None
        while start > 0:
            prev = dummy
            dummy = dummy.next
            start -= 1

        if prev is None:
            return dummy.next

        prev.next = dummy.next
        return head
