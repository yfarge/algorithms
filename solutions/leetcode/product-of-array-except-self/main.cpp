#include <vector>

class Solution {
public:
  std::vector<int> productExceptSelf(std::vector<int> &nums) {
    std::vector<int> result(nums.size());
    result[0] = 1;
    for (int i = 1; i < result.size(); i++) {
      result[i] = result[i - 1] * nums[i - 1];
    }
    int right = 1;
    for (int i = result.size() - 1; i >= 0; i--) {
      result[i] *= right;
      right *= nums[i];
    }
    return result;
  }
};
