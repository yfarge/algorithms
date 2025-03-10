#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
  int longestValidSubstring(string word, vector<string> &forbidden) {
    unordered_set<string> forbiddenSet(forbidden.begin(), forbidden.end());
    int left = 0, result = 0;
    for (int right = 0; right < word.size(); ++right) {
      for (int i = right; i >= max(left, right - 9); --i) {
        if (forbiddenSet.find(word.substr(i, right - i + 1)) !=
            forbiddenSet.end()) {
          left = i + 1;
        }
      }

      result = max(result, right - left + 1);
    }

    return result;
  }
};
