interface TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
}

export default function BSTLowestCommonAncestor(
  root: TreeNode | null,
  a: TreeNode | null,
  b: TreeNode | null,
): TreeNode | null {
  if (root == null || a == null || b == null) {
    return null;
  }

  if (a.val < root.val && b.val < root.val) {
    return BSTLowestCommonAncestor(root.left, a, b);
  }

  if (a.val > root.val && b.val > root.val) {
    return BSTLowestCommonAncestor(root.right, a, b);
  }

  return root;
}
