class Solution {
public:
  vector<int> topKFrequent(vector<int> &nums, int k) {
    unordered_map<int, int> counter;
    for (auto num : nums) {
      counter[num]++;
    }

    vector<vector<int>> buckets(nums.size());
    for (const auto &pair : counter) {
      buckets[pair.second - 1].push_back(pair.first);
    }

    vector<int> result;
    for (int i = buckets.size() - 1; i >= 0; i--) {
      for (auto value : buckets[i]) {
        result.push_back(value);
      }
      if (result.size() == k) {
        return result;
      }
    }
    return result;
  }
};
