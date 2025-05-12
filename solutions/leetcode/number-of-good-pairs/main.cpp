#include <unordered_map>
#include <vector>

using namespace std;

class Solution {
public:
  int numIdenticalPairs(vector<int> &nums) {
    int result = 0;
    unordered_map<int, int> seen;
    for (int i = 0; i < nums.size(); ++i) {
      if (seen.find(nums[i]) != seen.end()) {
        result += seen[nums[i]];
      }
      seen[nums[i]]++;
    }
    return result;
  }
};
