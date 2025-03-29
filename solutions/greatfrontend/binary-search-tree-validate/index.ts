interface TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

export default function binarySearchTreeValidate(
    root: TreeNode | null,
): boolean {
    function validate(node: TreeNode | null, minimum: number, maximum: number): boolean {
        if (node == null) {
            return true;
        }

        if (node.val < minimum || node.val > maximum) {
            return false;
        }

        const left = validate(node.left, minimum, Math.min(maximum, node.val));
        const right = validate(node.right, Math.max(minimum, node.val), maximum);

        return left && right;
    }

    return validate(root, -Infinity, Infinity)
}
