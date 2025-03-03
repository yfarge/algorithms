#include <vector>

class Solution {
public:
  int maxProfit(std::vector<int> &prices) {
    int minLeft[prices.size()];
    minLeft[0] = prices[0];

    for (int i = 1; i < prices.size(); i++) {
      minLeft[i] = std::min(minLeft[i - 1], prices[i]);
    }

    int result = 0;
    for (int i = 0; i < prices.size(); i++) {
      result = std::max(result, prices[i] - minLeft[i]);
    }

    return result;
  }
};
