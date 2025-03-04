#include <string>
using namespace std;

class Solution {
public:
  bool checkInclusion(string s1, string s2) {
    if (s1.size() > s2.size()) {
      return false;
    }

    int c1[26] = {0}, c2[26] = {0};
    for (int i = 0; i < s1.size(); i++) {
      c1[s1[i] - 'a']++;
      c2[s2[i] - 'a']++;
    }

    int matches = 0;
    for (int i = 0; i < 26; i++) {
      matches += c1[i] == c2[i];
    }

    int left = 0;
    for (int right = s1.size(); right < s2.size(); right++) {
      if (matches == 26) {
        return true;
      }

      int index = s2[right] - 'a';
      c2[index]++;
      if (c1[index] == c2[index]) {
        matches++;
      } else if (c1[index] + 1 == c2[index]) {
        matches--;
      }

      index = s2[left] - 'a';
      c2[index]--;
      if (c1[index] == c2[index]) {
        matches++;
      } else if (c1[index] - 1 == c2[index]) {
        matches--;
      }
      left++;
    }

    return matches == 26;
  }
};
