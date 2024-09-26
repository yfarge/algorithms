from typing import Optional
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, total):
            nonlocal count
            if node:
                current_sum = total + node.val
                if current_sum == targetSum:
                    count += 1

                count += prefix_sum[current_sum - targetSum]
                prefix_sum[current_sum] += 1

                dfs(node.left, current_sum)
                dfs(node.right, current_sum)
                prefix_sum[current_sum] -= 1

        count = 0
        prefix_sum = defaultdict(int)
        dfs(root, 0)

        return count
