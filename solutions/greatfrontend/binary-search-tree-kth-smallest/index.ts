interface TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

export default function kthSmallestElementInABst(
    root: TreeNode | null,
    k: number,
): number {
    function inorder(node: TreeNode | null): number[] {
        if (node == null) {
            return [];
        }
        const left = inorder(node.left);
        const right = inorder(node.right);

        return [...left, node.val, ...right];
    }

    return inorder(root)[k - 1];
}
