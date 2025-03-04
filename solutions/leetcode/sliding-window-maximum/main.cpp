#include <deque>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> maxSlidingWindow(vector<int> &nums, int k) {
    deque<int> queue;
    vector<int> result;
    int left = 0;
    for (int right = 0; right < nums.size(); right++) {
      while (!queue.empty() && nums[queue.back()] < nums[right]) {
        queue.pop_back();
      }

      queue.push_back(right);

      if (left > queue.front()) {
        queue.pop_front();
      }

      if (right + 1 >= k) {
        result.push_back(nums[queue.front()]);
        left++;
      }
    }
    return result;
  }
};
