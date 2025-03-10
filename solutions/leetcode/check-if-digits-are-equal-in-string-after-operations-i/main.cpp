#include <string>

using namespace std;

class Solution {
public:
  bool hasSameDigits(string s) {
    string tmp = "";
    while (s.size() > 2) {
      tmp.clear();
      for (int i = 2; i <= s.size(); i++) {
        int lhs = s[i - 2] - '0';
        int rhs = s[i - 1] - '0';
        tmp += (lhs + rhs) % 10;
      }
      s = tmp;
    }

    return s[s.size() - 1] == s[s.size() - 2];
  }
};
