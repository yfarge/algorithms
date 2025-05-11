#include <unordered_map>
#include <vector>

using namespace std;

template <typename T> class SparseVector {
private:
  unordered_map<int, T> data;

public:
  const T operator[](size_t index) const {
    auto it = data.find(index);
    return it != data.end() ? it->second : T{};
  }

  SparseVector(vector<T> &nums) {
    for (int i = 0; i < nums.size(); ++i) {
      if (nums[i] == 0)
        continue;
      data[i] = nums[i];
    }
  }

  // Return the dotProduct of two sparse vectors
  int dotProduct(SparseVector &vec) {
    int result = 0;
    for (const auto &[key, value] : data) {
      result += value * vec[key];
    }
    return result;
  }
};

// Your SparseVector object will be instantiated and called as such:
// SparseVector v1(nums1);
// SparseVector v2(nums2);
// int ans = v1.dotProduct(v2);
