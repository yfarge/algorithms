#include <vector>

using namespace std;

class Solution {
public:
    int maximumWealth(vector<vector<int>>& accounts) {
        int result = 0;
        int current = 0;
        for (int i = 0; i < accounts.size(); ++i) {
            current = 0;
            for (int j = 0; j < accounts[0].size(); ++j) {
                current += accounts[i][j];
            }
            result = max(result, current);
        }
        return result;
    }
};
