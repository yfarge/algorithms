class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_terminal = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_terminal = True

    def search(self, word: str) -> bool:
        def dfs(node: TrieNode, index: int):
            if index == len(word):
                return node.is_terminal

            char = word[index]
            if char == '.':
                return any(dfs(child, index + 1) for child in node.children.values())

            if char in node.children:
                return dfs(node.children[char], index + 1)

            return False

        return dfs(self.root, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
