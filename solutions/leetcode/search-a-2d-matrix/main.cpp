#include <vector>

using namespace std;

class Solution {
public:
  bool searchMatrix(vector<vector<int>> &matrix, int target) {
    int m = matrix.size(), n = matrix[0].size();
    int low = 0, high = m * n - 1;
    while (low <= high) {
      int mid = low + (high - low) / 2;
      int row = mid / n, col = mid % n;

      if (matrix[row][col] < target) {
        low = mid + 1;
      } else if (matrix[row][col] > target) {
        high = mid - 1;
      } else {
        return true;
      }
    }
    return false;
  }
};
