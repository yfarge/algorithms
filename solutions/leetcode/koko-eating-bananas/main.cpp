#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
  int minEatingSpeed(vector<int> &piles, int h) {
    int low = 1, high = *max_element(piles.begin(), piles.end());

    while (low <= high) {
      int k = low + (high - low) / 2;

      long long timeSpent = 0;
      for (int pile : piles) {
        timeSpent += (pile + k - 1) / k;
      }

      if (timeSpent <= h) {
        high = k - 1;
      } else {
        low = k + 1;
      }
    }

    return low;
  }
};
