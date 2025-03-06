#include <stack>

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
  TreeNode *invertTree(TreeNode *root) {
    if (root == nullptr) {
      return nullptr;
    }

    stack<TreeNode *> stack;
    stack.push(root);

    while (!stack.empty()) {
      TreeNode *node = stack.top();
      stack.pop();

      if (node->left != nullptr) {
        stack.push(node->left);
      }

      if (node->right != nullptr) {
        stack.push(node->right);
      }

      TreeNode *tmp = node->left;
      node->left = node->right;
      node->right = tmp;
    }
    return root;
  }
};
