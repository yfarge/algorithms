from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head:
            return

        node = head
        while node.next:
            d = ListNode(self.gcd(node.val, node.next.val))
            tmp = node.next
            node.next = d
            d.next = tmp
            node = tmp

        return head

    def gcd(self, a: int, b: int):
        while b != 0:
            a, b = b, a % b
        return a
