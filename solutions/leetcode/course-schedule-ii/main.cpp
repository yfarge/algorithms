#include <algorithm>
#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
  vector<int> findOrder(int numCourses, vector<vector<int>> &prerequisites) {
    vector<int> indegree(numCourses, 0);
    vector<vector<int>> adj(numCourses);

    for (auto &edge : prerequisites) {
      indegree[edge[1]]++;
      adj[edge[0]].push_back(edge[1]);
    }

    queue<int> queue;
    for (int i = 0; i < numCourses; i++) {
      if (indegree[i] == 0) {
        queue.push(i);
      }
    }

    vector<int> result;
    while (!queue.empty()) {
      int course = queue.front();
      queue.pop();
      result.push_back(course);
      for (int nei : adj[course]) {
        indegree[nei]--;
        if (indegree[nei] == 0) {
          queue.push(nei);
        }
      }
    }

    if (result.size() == numCourses) {
      reverse(result.begin(), result.end());
      return result;
    }

    return {};
  }
};
