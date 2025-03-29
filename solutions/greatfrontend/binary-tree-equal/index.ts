interface TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

export default function binaryTreeEqual(
    a: TreeNode | null,
    b: TreeNode | null,
): boolean {
    if (a == null && b == null) {
        return true;
    }

    if (a != null && b == null || a == null && b != null) {
        return false;
    }

    return (
        a != null && b != null && a.val == b.val &&
        binaryTreeEqual(a.left, b.left) && binaryTreeEqual(a.right, b.right))
}
