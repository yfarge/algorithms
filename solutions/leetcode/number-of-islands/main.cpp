#include <deque>
#include <vector>

using namespace std;

class Solution {
public:
  int offsets[4][2] = {{0, -1}, {-1, 0}, {0, 1}, {1, 0}};
  int numIslands(vector<vector<char>> &grid) {
    deque<pair<int, int>> queue;

    int count = 0;
    for (int r = 0; r < grid.size(); r++) {
      for (int c = 0; c < grid[0].size(); c++) {
        if (grid[r][c] == '1') {
          bfs(grid, queue, r, c);
          count += 1;
        }
      }
    }

    return count;
  }

  void bfs(vector<vector<char>> &grid, deque<pair<int, int>> &queue, int r,
           int c) {
    queue.emplace_back(r, c);
    grid[r][c] = '0';

    while (!queue.empty()) {
      auto [currentRow, currentCol] = queue.front();
      queue.pop_front();

      for (int i = 0; i < 4; i++) {
        int nr = currentRow + offsets[i][0];
        int nc = currentCol + offsets[i][1];
        if (nr >= 0 && nr < grid.size() && nc >= 0 && nc < grid[0].size() &&
            grid[nr][nc] == '1') {
          queue.emplace_back(nr, nc);
          grid[nr][nc] = '0';
        }
      }
    }
  }
};
