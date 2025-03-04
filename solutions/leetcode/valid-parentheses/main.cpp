#include <stack>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
  bool isValid(string s) {
    stack<char> stack;
    unordered_map<char, char> brackets = {
        {')', '('},
        {'}', '{'},
        {']', '['},
    };

    for (char c : s) {
      if (brackets.find(c) == brackets.end()) {
        stack.push(c);
      } else if (!stack.empty() && stack.top() == brackets[c]) {
        stack.pop();
      } else {
        return false;
      }
    }

    return stack.empty();
  }
};
