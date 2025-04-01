interface TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

export default function binaryTreeMaximumDepth(root: TreeNode | null): number {
    if (root == null) {
        return 0;
    }

    const left = binaryTreeMaximumDepth(root.left);
    const right = binaryTreeMaximumDepth(root.right);

    return 1 + Math.max(left, right);
}
