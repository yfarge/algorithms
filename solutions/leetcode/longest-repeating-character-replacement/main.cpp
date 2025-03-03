#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
  int characterReplacement(string s, int k) {
    unordered_map<char, int> counter;
    int result = 0;
    int left = 0;
    int maxFrequency = 0;
    for (int right = 0; right < s.size(); right++) {
      counter[s[right]]++;
      maxFrequency = std::max(maxFrequency, counter[s[right]]);
      while (right - left + 1 - maxFrequency > k) {
        counter[s[left]]--;
        left++;
      }

      result = std::max(result, right - left + 1);
    }
    return result;
  }
};
