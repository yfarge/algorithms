#include <vector>

class Solution {
public:
  int trap(std::vector<int> &height) {
    std::vector<int> left(height.size());
    std::vector<int> right(height.size());

    for (int i = 1; i < height.size(); i++) {
      left[i] = std::max(left[i - 1], height[i - 1]);
    }

    for (int i = height.size() - 2; i >= 0; i--) {
      right[i] = std::max(right[i + 1], height[i + 1]);
    }

    int result = 0;
    for (int i = 0; i < height.size(); i++) {
      int min_height = std::min(left[i], right[i]);
      int area = std::max(min_height - height[i], 0);
      result += area;
    }
    return result;
  }
};
