interface TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

// Encodes a tree to a single string
export function serializeBinaryTree(root: TreeNode | null): string {
    if (!root) return "";

    const result: string[] = [];
    const queue: (TreeNode | null)[] = [root]

    while (queue.length > 0) {
        const node = queue.shift();

        if (node == null) {
            result.push("null");
        } else {
            result.push(node.val.toString());
            queue.push(node.left);
            queue.push(node.right);
        }
    }

    return result.join(",");
}

// Decodes your encoded data to tree
export function deserializeBinaryTree(data: string): TreeNode | null {
    if (!data) return null;

    const levelOrder = data.split(',').map((val) => val == 'null' ? null : Number(val));

    const root: TreeNode = { val: levelOrder[0]!, left: null, right: null };
    const queue = [root];
    let index = 1;

    while (index < levelOrder.length) {
        const node = queue.shift()!;

        if (index < levelOrder.length && levelOrder[index] != null) {
            node.left = { val: levelOrder[index] as number, left: null, right: null };
            queue.push(node.left);
        }
        index++;

        if (index < levelOrder.length && levelOrder[index] != null) {
            node.right = { val: levelOrder[index] as number, left: null, right: null };
            queue.push(node.right);
        }
        index++;
    }

    return root;
}
