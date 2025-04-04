interface TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

export default function binaryTreeMaximumPathSum(root: TreeNode | null): number {
    let result = -Infinity;

    function dfs(node: TreeNode | null): number {
        if (!node) return 0;

        const leftMax = Math.max(dfs(node.left), 0);
        const rightMax = Math.max(dfs(node.right), 0);

        const localMax = node.val + leftMax + rightMax;

        result = Math.max(result, localMax);

        return node.val + Math.max(leftMax, rightMax);
    }

    dfs(root);
    return result;
}
