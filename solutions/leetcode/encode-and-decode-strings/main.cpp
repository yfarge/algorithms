class Codec {
public:
  // Encodes a list of strings to a single string.
  string encode(vector<string> &strs) {
    string result;
    for (const auto &s : strs) {
      result += to_string(s.size());
      result += "#";
      result += s;
    }
    return result;
  }

  // Decodes a single string to a list of strings.
  vector<string> decode(string s) {
    vector<string> result;
    int i = 0;
    while (i < s.size()) {
      int j = i;
      while (s[j] != '#') {
        j++;
      }
      int len = stoi(s.substr(i, j - i));
      result.push_back(s.substr(j + 1, len));
      i = j + len + 1;
    }
    return result;
  }
};

// Your Codec object will be instantiated and called as such:
// Codec codec;
// codec.decode(codec.encode(strs));
