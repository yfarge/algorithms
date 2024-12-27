from typing import Optional, List


# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class Solution:
    def toArray(self, root: Optional[Node]) -> List[int]:
        result = []
        while root:
            result.append(root.val)
            root = root.next
        return result
