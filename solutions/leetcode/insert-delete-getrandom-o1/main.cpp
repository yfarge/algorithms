#include <cstdlib>
#include <unordered_map>
#include <vector>

using namespace std;

class RandomizedSet {
public:
  unordered_map<int, int> indices;
  vector<int> values;

  RandomizedSet() {}

  bool insert(int val) {
    if (indices.find(val) != indices.end()) {
      return false;
    }

    values.push_back(val);
    indices[val] = values.size() - 1;
    return true;
  }

  bool remove(int val) {
    if (indices.find(val) == indices.end()) {
      return false;
    }
    int swapVal = values.back();
    int valIndex = indices[val];
    values[valIndex] = swapVal;
    indices[swapVal] = valIndex;
    indices.erase(val);
    values.pop_back();

    return true;
  }

  int getRandom() { return values[rand() % values.size()]; }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
