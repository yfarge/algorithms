#include <functional>
#include <stack>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
  int evalRPN(vector<string> &tokens) {
    unordered_map<string, function<int(int, int)>> operators = {
        {"+", [](int lhs, int rhs) { return lhs + rhs; }},
        {"-", [](int lhs, int rhs) { return lhs - rhs; }},
        {"*", [](int lhs, int rhs) { return lhs * rhs; }},
        {"/", [](int lhs, int rhs) { return lhs / rhs; }},
    };

    stack<int> stack;
    for (const auto &token : tokens) {
      if (operators.find(token) == operators.end()) {
        stack.push(stoi(token));
      } else {
        int rhs = stack.top();
        stack.pop();
        int lhs = stack.top();
        stack.pop();
        int result = operators[token](lhs, rhs);
        stack.push(result);
      }
    }
    return stack.top();
  }
};
