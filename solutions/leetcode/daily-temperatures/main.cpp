#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> dailyTemperatures(vector<int> &temperatures) {
    vector<int> result(temperatures.size(), 0);
    stack<int> stack;
    for (int i = 0; i < temperatures.size(); i++) {
      while (!stack.empty() && temperatures[stack.top()] < temperatures[i]) {
        int j = stack.top();
        stack.pop();
        result[j] = i - j;
      }
      stack.push(i);
    }
    return result;
  }
};
