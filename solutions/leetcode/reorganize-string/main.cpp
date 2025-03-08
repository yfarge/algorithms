#include <queue>
#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
  string reorganizeString(string s) {
    unordered_map<char, int> counter;
    for (char c : s) {
      counter[c]++;
    }

    priority_queue<pair<int, char>> pq;
    for (auto &[key, value] : counter) {
      pq.emplace(value, key);
    }

    string result = "";
    queue<pair<int, char>> queue;

    while (!pq.empty()) {
      auto [count, ch] = pq.top();
      pq.pop();
      result += ch;

      if (count > 1) {
        queue.emplace(count - 1, ch);
      }

      if (!queue.empty() && result.back() != queue.front().second) {
        pq.push(queue.front());
        queue.pop();
      }
    }

    return queue.size() == 0 ? result : "";
  }
};
