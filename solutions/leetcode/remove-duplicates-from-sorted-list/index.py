from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        current = head.next
        previous = head
        while current:
            if previous.val != current.val:
                previous = current
            previous.next = current.next
            current = current.next

        return head
