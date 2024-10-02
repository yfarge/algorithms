from collections import OrderedDict


# OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# Custom Doubly Linked List
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.entries = dict()
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.entries:
            return -1

        node = self.entries[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.entries:
            node = self.entries[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            node = ListNode(key, value)
            self.add(node)
            self.entries[key] = node

        if len(self.entries) > self.capacity:
            lru_node = self.head.next
            self.remove(lru_node)
            del self.entries[lru_node.key]

    def add(self, node: ListNode):
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node: ListNode):
        node.next.prev = node.prev
        node.prev.next = node.next
