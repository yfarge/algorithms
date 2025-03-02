#include <unordered_set>
#include <vector>

class Solution {
public:
  int longestConsecutive(std::vector<int> &nums) {
    std::unordered_set<int> lookup(nums.begin(), nums.end());
    int result = 0;
    for (auto num : lookup) {
      if (lookup.find(num - 1) == lookup.end()) {
        int curr_num = num;
        int curr_len = 1;
        while (lookup.count(curr_num + 1)) {
          curr_num += 1;
          curr_len += 1;
        }
        result = std::max(result, curr_len);
      }
    }
    return result;
  }
};
