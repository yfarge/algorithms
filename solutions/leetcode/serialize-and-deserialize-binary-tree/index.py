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

        def preorder(node):
            if not node:
                return [None]

            return [node.val] + preorder(node.left) + preorder(node.right)

        return str(preorder(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        preorder = eval(data)
        index = 0

        def create_binary_tree():
            nonlocal index
            if preorder[index] is None:
                return None

            node = TreeNode(preorder[index])

            index += 1
            node.left = create_binary_tree()

            index += 1
            node.right = create_binary_tree()

            return node

        return create_binary_tree()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
