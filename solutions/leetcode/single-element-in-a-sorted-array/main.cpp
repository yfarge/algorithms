#include <vector>

using namespace std;

class Solution {
public:
  int singleNonDuplicate(vector<int> &nums) {
    int left = 0, right = nums.size() - 1;

    while (left <= right) {
      int mid = left + (right - left) / 2;

      if (mid > 0 && nums[mid] == nums[mid - 1]) {
        int leftLength = left - mid + 1;
        if (leftLength % 2) {
          right = mid;
        } else {
          left = mid + 1;
        }
      } else if (mid < nums.size() - 1 && nums[mid] == nums[mid + 1]) {
        int rightLength = right - mid + 1;
        if (rightLength % 2) {
          left = mid;
        } else {
          right = mid - 1;
        }
      } else {
        return nums[mid];
      }
    }

    return nums[right];
  }
};
