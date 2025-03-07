#include <algorithm>

using namespace std;

// Definition for a binary tree node.
struct TreeNode {
  int val;
  TreeNode *left;
  TreeNode *right;
  TreeNode() : val(0), left(nullptr), right(nullptr) {}
  TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
  TreeNode(int x, TreeNode *left, TreeNode *right)
      : val(x), left(left), right(right) {}
};

class Solution {
public:
  bool isBalanced(TreeNode *root) {
    bool flag = true;
    dfs(root, flag);
    return flag;
  }

  int dfs(TreeNode *root, bool &flag) {
    if (root == nullptr || !flag) {
      return 0;
    }

    int left = dfs(root->left, flag);
    int right = dfs(root->right, flag);

    if (abs(right - left) > 1) {
      flag = false;
      return 0;
    }

    return 1 + max(left, right);
  }
};
