#include <vector>

using namespace std;

class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> result;
        for (int i = 0; i < words.size(); ++i) {
            string word =  words[i];
            for (const char &ch: word) {
                if (ch == x) {
                    result.push_back(i);
                    break;
                }
            }
        }
        return result;
    }
};
