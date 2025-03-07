#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
  int maxSubArray(vector<int> &nums) {
    int currentSum = nums[0], maxSum = nums[0];

    for (int i = 1; i < nums.size(); i++) {
      currentSum = max(nums[i], currentSum + nums[i]);
      maxSum = max(maxSum, currentSum);
    }

    return maxSum;
  }
};
