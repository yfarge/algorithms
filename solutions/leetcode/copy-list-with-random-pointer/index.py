from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copied = {}
        current = head

        while current:
            node = copied.setdefault(current, Node(current.val))

            if current.next:
                node.next = copied.setdefault(
                    current.next, Node(current.next.val))

            if current.random:
                node.random = copied.setdefault(
                    current.random, Node(current.random.val))

            current = current.next

        return copied.get(head)
