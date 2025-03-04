#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  vector<string> generateParenthesis(int n) {
    vector<string> result;
    string stack;
    backtrack(0, 0, n, result, stack);
    return result;
  }

  void backtrack(int openN, int closedN, int n, vector<string> &result,
                 string &stack) {
    if (openN == closedN && openN == n) {
      result.push_back(stack);
    }

    if (openN < n) {
      stack += '(';
      backtrack(openN + 1, closedN, n, result, stack);
      stack.pop_back();
    }

    if (closedN < openN) {
      stack += ')';
      backtrack(openN, closedN + 1, n, result, stack);
      stack.pop_back();
    }
  }
};
