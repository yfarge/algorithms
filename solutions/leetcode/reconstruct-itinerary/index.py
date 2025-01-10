from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = {u: [] for u, v in tickets}
        tickets.sort()
        for u, v in tickets:
            graph[u].append(v)

        res = ["JFK"]

        def dfs(u: int):
            if len(res) == len(tickets) + 1:
                return True

            if u not in graph:
                return False

            temp = list(graph[u])
            for i, v in enumerate(temp):
                graph[u].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                graph[u].insert(i, v)
                res.pop()
            return False

        dfs("JFK")
        return res
