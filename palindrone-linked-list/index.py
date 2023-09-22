from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find the node in the middle of the linked list
        middle, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            middle = middle.next

        # reverse the second half of the linked list
        curr = middle
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        middle = prev

        # compare the first and second half of the linked list
        while middle is not None:
            if middle.val != head.val:
                return False
            middle = middle.next
            head = head.next

        return True
