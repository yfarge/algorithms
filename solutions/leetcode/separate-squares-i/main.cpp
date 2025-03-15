#include <vector>

using namespace std;

class Solution {
public:
  double separateSquares(vector<vector<int>> &squares) {
    double left = 0, right = 1e9;
    while (right - left >= 1e-5) {
      double mid = left + (right - left) / 2.0;
      double diff = difference(mid, squares);
      if (diff > 0) {
        left = mid;
      } else {
        right = mid;
      }
    }
    return right;
  }

  double difference(double mid, vector<vector<int>> &squares) {
    double above = 0, below = 0;
    for (int i = 0; i < squares.size(); ++i) {
      int x = squares[i][0], y = squares[i][1], l = squares[i][2];
      double area = (double)l * l;
      if (y >= mid) {
        above += area;
      } else if (y + l <= mid) {
        below += area;
      } else {
        double aHeight = (y + l) - mid;
        double bHeight = mid - y;
        above += aHeight * l;
        below += bHeight * l;
      }
    }
    return above - below;
  }
};
