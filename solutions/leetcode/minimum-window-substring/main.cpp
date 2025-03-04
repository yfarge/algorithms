#include <climits>
#include <string>

using namespace std;

class Solution {
public:
  string minWindow(string s, string t) {
    if (t.size() > s.size())
      return "";

    int current[128] = {0}, target[128] = {0};
    int need = 0;
    for (char c : t) {
      if (target[c] == 0)
        need++;
      target[c]++;
    }

    int left = 0, start = 0, minLength = INT_MAX, have = 0;
    for (int right = 0; right < s.size(); right++) {
      current[s[right]]++;
      if (current[s[right]] == target[s[right]])
        have++;

      while (have == need) {
        if (right - left + 1 < minLength) {
          minLength = right - left + 1;
          start = left;
        }
        current[s[left]]--;
        if (current[s[left]] < target[s[left]]) {
          have--;
        }
        left++;
      }
    }

    return (minLength == INT_MAX) ? "" : s.substr(start, minLength);
  }
};
