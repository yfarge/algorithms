interface TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

export default function binaryTreeRebuildingFromTraversals(
    preorder: number[],
    inorder: number[],
): TreeNode | null {
    function dfs(left: number, right: number): TreeNode | null {
        if (right < left) {
            return null;
        }

        const root: TreeNode = { val: preorder[preorderIndex], left: null, right: null };
        const inorderIndex = inorderIndexMap[root.val];

        preorderIndex++;

        root.left = dfs(left, inorderIndex - 1);
        root.right = dfs(inorderIndex + 1, right);

        return root;
    }

    let preorderIndex = 0;
    const inorderIndexMap: Record<number, number> = {};
    for (let i = 0; i < inorder.length; ++i) {
        inorderIndexMap[inorder[i]] = i;
    }

    return dfs(0, preorder.length - 1);
}
