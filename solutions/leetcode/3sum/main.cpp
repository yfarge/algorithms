#include <algorithm>
#include <vector>

class Solution {
public:
  std::vector<std::vector<int>> threeSum(std::vector<int> &nums) {
    std::sort(nums.begin(), nums.end());
    std::vector<std::vector<int>> result;
    for (int i = 0; i < nums.size(); i++) {
      if (i > 0 && nums[i] == nums[i - 1]) {
        continue;
      }

      int j = i + 1, k = nums.size() - 1;

      while (j < k) {
        int total = nums[i] + nums[j] + nums[k];

        if (total == 0) {
          result.push_back({nums[i], nums[j], nums[k]});
          j++;
          k--;
          while (j < k && nums[j] == nums[j - 1]) {
            j++;
          }
          while (j < k && nums[k] == nums[k + 1]) {
            k--;
          }
        } else if (total < 0) {
          j++;
        } else {
          k--;
        }
      }
    }
    return result;
  }
};
