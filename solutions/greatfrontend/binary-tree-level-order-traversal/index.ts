interface TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

export default function binaryTreeLevelOrderTraversal(
    root: TreeNode | null,
): number[][] {
    if (root == null) {
        return [];
    }

    const result: number[][] = [];
    const stack: [TreeNode | null, number][] = [[root, 0]];
    while (stack.length > 0) {
        const [node, depth] = stack.pop() || [];
        if (node == null || depth == null) {
            continue;
        }

        if (result.length == depth) {
            result.push([])
        }

        stack.push([node.right, depth + 1])
        stack.push([node.left, depth + 1])

        result[depth].push(node.val)
    }

    return result;
}
