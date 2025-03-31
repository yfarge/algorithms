interface TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

export default function binaryTreeFlip(root: TreeNode | null): TreeNode | null {
    if (root == null) {
        return null;
    }

    const tmp = root.left
    root.left = binaryTreeFlip(root.right)
    root.right = binaryTreeFlip(tmp)

    return root
}
