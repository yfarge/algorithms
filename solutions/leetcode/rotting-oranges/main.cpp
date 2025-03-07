#include <deque>
#include <vector>

using namespace std;

class Solution {
public:
  int orangesRotting(vector<vector<int>> &grid) {
    int ROWS = grid.size(), COLS = grid[0].size();
    int offsets[4][2] = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
    deque<pair<int, int>> queue;

    int fresh = 0;
    for (int r = 0; r < ROWS; r++) {
      for (int c = 0; c < COLS; c++) {
        if (grid[r][c] == 2) {
          queue.emplace_back(r, c);
        } else {
          fresh += grid[r][c];
        }
      }
    }

    int minutes = 0;
    while (!queue.empty() && fresh > 0) {
      minutes += 1;
      int n = queue.size();
      for (int i = 0; i < n; i++) {
        auto [cr, cc] = queue.front();
        queue.pop_front();

        for (int j = 0; j < 4; j++) {
          int nr = cr + offsets[j][0];
          int nc = cc + offsets[j][1];

          if (nr >= 0 && nr < ROWS && nc >= 0 && nc < COLS &&
              grid[nr][nc] == 1) {
            queue.emplace_back(nr, nc);
            grid[nr][nc] = 2;
            fresh--;
          }
        }
      }
    }
    return fresh == 0 ? minutes : -1;
  }
};
