interface TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
}

export default function binaryTreeLevelOrderTraversal(
  root: TreeNode | null,
): number[][] {
  const result: number[][] = [];
  function dfs(node: TreeNode | null, depth: number) {
    if (node == null) {
      return
    }

    if (result.length == depth) {
      result.push(Array());
    }

    dfs(node.left, depth + 1)
    dfs(node.right, depth + 1)

    result[depth].push(node.val);
  }

  dfs(root, 0);

  return result;
}
