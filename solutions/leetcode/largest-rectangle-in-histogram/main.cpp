#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
  int largestRectangleArea(vector<int> &heights) {
    stack<pair<int, int>> stack;
    int result = 0, n = heights.size();
    for (int i = 0; i < n; i++) {
      int start = i;
      while (!stack.empty() && stack.top().second > heights[i]) {
        auto [j, h] = stack.top();
        stack.pop();
        result = max(result, h * (i - j));
        start = j;
      }
      stack.push({start, heights[i]});
    }

    while (!stack.empty()) {
      auto [j, h] = stack.top();
      stack.pop();
      result = max(result, h * (n - j));
    }

    return result;
  }
};
