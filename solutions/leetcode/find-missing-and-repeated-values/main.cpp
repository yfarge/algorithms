#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> findMissingAndRepeatedValues(vector<vector<int>> &grid) {
    unordered_set<int> seen;
    int m = grid.size(), n = grid[0].size();
    int repeated = 0;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (seen.find(grid[i][j]) != seen.end()) {
          repeated = grid[i][j];
        }
        seen.insert(grid[i][j]);
      }
    }

    int missing = 0;
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        if (seen.find(i * n + j + 1) == seen.end()) {
          missing = i * n + j + 1;
          break;
        }
      }
    }

    return {repeated, missing};
  }
};
