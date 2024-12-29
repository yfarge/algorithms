from typing import List, Optional


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_terminal = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_terminal = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        m, n = len(board), len(board[0])
        result, visited = set(), set()
        path = []

        def dfs(row: int, col: int, node: Optional[TrieNode]):
            if (
                row < 0
                or m <= row
                or col < 0
                or n <= col
                or (row, col) in visited
                or board[row][col] not in node.children
            ):
                return None

            visited.add((row, col))
            path.append(board[row][col])
            node = node.children[board[row][col]]

            if node.is_terminal:
                result.add("".join(path))

            dfs(row, col - 1, node)
            dfs(row - 1, col, node)
            dfs(row, col + 1, node)
            dfs(row + 1, col, node)
            visited.discard((row, col))
            path.pop()

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root)

        return list(result)
