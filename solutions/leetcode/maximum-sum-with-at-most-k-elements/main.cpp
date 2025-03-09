#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
  long long maxSum(vector<vector<int>> &grid, vector<int> &limits, int k) {
    priority_queue<int> pq;

    for (int r = 0; r < grid.size(); r++) {
      sort(grid[r].begin(), grid[r].end(), greater<int>());
      for (int c = 0; c < limits[r]; c++) {
        pq.push(grid[r][c]);
      }
    }

    long long result = 0;
    while (k > 0) {
      result += pq.top();
      pq.pop();
      k--;
    }
    return result;
  }
};
