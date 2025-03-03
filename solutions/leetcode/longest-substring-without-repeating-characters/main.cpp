#include <string>
#include <unordered_map>

using namespace std;

class Solution {
public:
  int lengthOfLongestSubstring(string s) {
    unordered_map<char, int> seen;
    int result = 0;
    int left = 0;
    for (int right = 0; right < s.size(); right++) {
      if (seen.find(s[right]) != seen.end()) {
        left = std::max(left, seen[s[right]] + 1);
      }
      seen[s[right]] = right;
      result = std::max(result, right - left + 1);
    }
    return result;
  }
};
