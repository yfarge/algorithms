from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next

        nodes.sort(key=lambda n: n.val)

        for i in range(1, len(nodes)):
            nodes[i - 1].next = nodes[i]

        nodes[-1].next = None

        return nodes[0]
