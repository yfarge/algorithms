#include <map>
#include <vector>

using namespace std;

class Solution {
public:
  vector<vector<int>> mergeArrays(vector<vector<int>> &nums1,
                                  vector<vector<int>> &nums2) {
    map<int, int> sums;
    for (int i = 0; i < nums1.size(); ++i) {
      sums[nums1[i][0]] += nums1[i][1];
    }

    for (int i = 0; i < nums2.size(); ++i) {
      sums[nums2[i][0]] += nums2[i][1];
    }

    vector<vector<int>> result;
    for (auto &pair : sums) {
      result.push_back({pair.first, pair.second});
    }

    return result;
  }
};
