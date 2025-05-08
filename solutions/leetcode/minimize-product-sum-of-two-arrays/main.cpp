#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
  int minProductSum(vector<int> &nums1, vector<int> &nums2) {
    std::sort(nums1.begin(), nums1.end(), [](int &a, int &b) { return a < b; });
    std::sort(nums2.begin(), nums2.end(), [](int &a, int &b) { return b < a; });

    int result = 0;
    for (int i = 0; i < nums1.size(); ++i) {
      result += nums1[i] * nums2[i];
    }

    return result;
  }
};
