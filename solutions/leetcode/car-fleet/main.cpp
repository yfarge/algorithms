#include <algorithm>
#include <stack>
#include <vector>

using namespace std;

class Solution {
public:
  int carFleet(int target, vector<int> &position, vector<int> &speed) {
    vector<int> indices(position.size());
    for (int i = 0; i < indices.size(); i++) {
      indices[i] = i;
    }

    sort(indices.begin(), indices.end(),
         [&position](int a, int b) { return position[a] < position[b]; });

    stack<double> stack;
    for (int i : indices) {
      double step = (double)(target - position[i]) / speed[i];
      while (!stack.empty() && stack.top() <= step) {
        stack.pop();
      }
      stack.push(step);
    }

    return stack.size();
  }
};
