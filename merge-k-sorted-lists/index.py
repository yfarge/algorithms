from queue import PriorityQueue


# Wrapper to add less than operator to ListNode class
class Wrapper():
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution
class Solution(object):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """

    def mergeKLists(self, lists: list[ListNode]):
        cur = dummy = ListNode()
        q = PriorityQueue()

        for l in [l for l in lists if l is not None]:
            q.put(Wrapper(l))

        while not q.empty():
            l = q.get().node
            cur.next = l
            cur = cur.next
            l = l.next
            if l:
                q.put(Wrapper(l))

        return dummy.next
