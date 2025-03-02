#include <vector>

class Solution {
public:
  int maxArea(std::vector<int> &height) {
    int left = 0, right = height.size() - 1;
    int result = 0;
    while (left < right) {
      int width = right - left;
      int min_height = std::min(height[left], height[right]);
      result = std::max(result, width * min_height);

      if (height[left] < height[right]) {
        left++;
      } else if (height[right] < height[left]) {
        right--;
      } else {
        left++;
        right--;
      }
    }
    return result;
  }
};
