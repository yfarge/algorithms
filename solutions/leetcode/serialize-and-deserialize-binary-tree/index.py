from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""

        result = []

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                result.append('#')
                continue
            result.append(str(node.val))

            queue.append(node.left)
            queue.append(node.right)

        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = data.split(',')
        root = TreeNode(int(data[0]))
        i = 1
        queue = deque([root])
        while queue and i < len(data):
            node = queue.popleft()

            if data[i] != '#':
                node.left = TreeNode(int(data[i]))
                queue.append(node.left)
            i += 1

            if i < len(data) and data[i] != '#':
                node.right = TreeNode(int(data[i]))
                queue.append(node.right)
            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
