#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

class TimeMap {
private:
  unordered_map<string, vector<pair<int, string>>> d;

public:
  TimeMap() {}

  void set(string key, string value, int timestamp) {
    d[key].push_back({timestamp, value});
  }

  string get(string key, int timestamp) {
    if (d.find(key) == d.end()) {
      return "";
    }

    vector<pair<int, string>> &pairs = d.find(key)->second;
    int left = 0, right = pairs.size() - 1;
    while (left <= right) {
      int mid = left + (right - left) / 2;
      if (pairs[mid].first < timestamp) {
        left = mid + 1;
      } else if (pairs[mid].first > timestamp) {
        right = mid - 1;
      } else {
        return pairs[mid].second;
      }
    }

    return right >= 0 ? pairs[right].second : "";
  }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */
