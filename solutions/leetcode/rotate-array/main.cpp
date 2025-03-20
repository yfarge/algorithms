#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
  void rotate(vector<int> &nums, int k) {
    int steps = k % nums.size();
    reverse(nums.begin(), nums.end() - steps);
    reverse(nums.end() - steps, nums.end());
    reverse(nums.begin(), nums.end());
  }
};
