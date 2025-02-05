from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = node = ListNode()
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            s = v1 + v2 + carry

            val = s % 10
            carry = s // 10
            node.next = ListNode(val)

            node = node.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

        return result.next
