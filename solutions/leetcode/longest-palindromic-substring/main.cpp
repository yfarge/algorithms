#include <string>

using namespace std;

class Solution {
public:
  string longestPalindrome(string s) {
    auto expandFromCenter = [&](int left, int right) -> string {
      while (left >= 0 && right < s.length() && s[left] == s[right]) {
        left--;
        right++;
      }
      return s.substr(left + 1, right - left - 1);
    };

    string longest_palindrome = "";
    for (int i = 0; i < s.length(); i++) {
      string odd_palindrome = expandFromCenter(i, i);
      string even_palindrome = expandFromCenter(i, i + 1);

      if (odd_palindrome.length() > longest_palindrome.length()) {
        longest_palindrome = odd_palindrome;
      }
      if (even_palindrome.length() > longest_palindrome.length()) {
        longest_palindrome = even_palindrome;
      }
    }

    return longest_palindrome;
  }
};
