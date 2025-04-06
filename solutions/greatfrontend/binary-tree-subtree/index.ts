interface TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

export default function binaryTreeSubtree(
    root: TreeNode | null,
    subRoot: TreeNode | null,
): boolean {
    function isIdentical(a: TreeNode | null, b: TreeNode | null): boolean {
        if (a == null || b == null) {
            return a === null && b === null;
        }

        return (
            a.val === b.val &&
            isIdentical(a.left, b.left) &&
            isIdentical(a.right, b.right)
        )
    }

    function dfs(root: TreeNode | null, subRoot: TreeNode | null): boolean {
        if (root == null) {
            return false;
        }

        if (isIdentical(root, subRoot)) {
            return true;
        }

        return (
            dfs(root.left, subRoot) || dfs(root.right, subRoot)
        )
    }

    return dfs(root, subRoot);
}
