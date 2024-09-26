from typing import List, Optional
from collections import defaultdict


class Node:
    def __init__(self):
        self.children = defaultdict(str)
        self.is_terminal = False


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

    def startsWith(self, word: str) -> Optional[Node]:
        node = self.root
        for c in word:
            if not node.children[c]:
                return None
            node = node.children[c]
        return node

    def search(self, query: str) -> List[str]:
        def dfs(node: Optional[Node], word: List[str]):
            if not node:
                return

            if node.is_terminal:
                suggestions.append("".join(word))

            for char, child in node.children.items():
                word.append(char)
                dfs(child, word)
                word.pop()

        node = self.startsWith(query)
        if not node:
            return []

        suggestions = []
        dfs(node, [*query])
        return sorted(suggestions)[0:3]


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        trie = Trie()

        for product in products:
            trie.insert(product)

        answer = []
        for query in [searchWord[0: i + 1] for i in range(len(searchWord))]:
            answer.append(trie.search(query))

        return answer


# Two Pointer
class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        answer = []
        products.sort()
        l, r = 0, len(products) - 1
        for i in range(len(searchWord)):
            c = searchWord[i]

            while l <= r and (len(products[l]) <= i or products[l][i] != c):
                l += 1

            while l <= r and (len(products[r]) <= i or products[r][i] != c):
                r -= 1

            suggestions = []
            for j in range(min(3, r - l + 1)):
                suggestions.append(products[l + j])
            answer.append(suggestions)

        return answer
