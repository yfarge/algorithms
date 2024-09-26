from collections import defaultdict


class Node:
    def __init__(self, is_terminal: bool = False):
        self.children = defaultdict(str)
        self.is_terminal = is_terminal


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if not node.children[c]:
                node.children[c] = Node()
            node = node.children[c]
        node.is_terminal = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if not node.children[c]:
                return False
            node = node.children[c]
        return node.is_terminal

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if not node.children[c]:
                return False
            node = node.children[c]
        return True
