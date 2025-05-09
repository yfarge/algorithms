# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
class ImmutableListNode:
    def printValue(self) -> None:  # print the value of this node.
        pass

    def getNext(self) -> 'ImmutableListNode':  # return the next node.
        pass


class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.getNext()

        for node in reversed(stack):
            node.printValue()
