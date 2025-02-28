class Solution {
public:
  vector<vector<string>> groupAnagrams(vector<string> &strs) {
    unordered_map<string, vector<string>> groups;
    int count[26];
    for (const auto &s : strs) {
      fill(begin(count), end(count), 0);
      for (char c : s)
        count[c - 'a']++;
      string group = "";
      for (int i = 0; i < 26; i++) {
        group += "#";
        group += to_string(count[i]);
      }
      groups[group].push_back(s);
    }

    vector<vector<string>> result;
    for (const auto &pair : groups) {
      result.push_back(pair.second);
    }

    return result;
  }
};
