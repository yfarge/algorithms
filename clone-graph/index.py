from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        visited = {}

        def dfs(node: Optional[Node]):
            if not node:
                return node

            if node in visited:
                return visited[node]

            cloned_node = Node(node.val, [])
            visited[node] = cloned_node

            for neighbor in node.neighbors:
                cloned_node.neighbors.append(dfs(neighbor))

            return cloned_node

        return dfs(node)
