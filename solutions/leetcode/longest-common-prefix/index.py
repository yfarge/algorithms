from typing import List


class Node:
    def __init__(self):
        self.children = {}
        self.isTerminal = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.isTerminal = True

    def longestPrefix(self):
        result = []
        node = self.root
        while len(node.children) == 1 and not node.isTerminal:
            char, node = list(node.children.items())[0]
            result.append(char)
        return "".join(result)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for s in strs:
            trie.insert(s)

        return trie.longestPrefix()
