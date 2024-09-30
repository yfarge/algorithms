from typing import List
from collections import defaultdict


# DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def detectCycle(course: int):
            visited[course] = True
            rec_stack[course] = True

            for neighbor in graph[course]:
                if not visited[neighbor]:
                    if detectCycle(neighbor):
                        return True
                elif rec_stack[neighbor]:
                    return True

            rec_stack[course] = False
            return False

        graph = defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)

        visited = defaultdict(bool)
        rec_stack = defaultdict(bool)
        for course in range(numCourses - 1):
            if not visited[course] and detectCycle(course):
                return False
        return True


# Topological Sort (Kahn's Algorithm)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)

        indegree = [0] * numCourses
        for i in range(numCourses):
            for neighbor in graph[i]:
                indegree[neighbor] += 1

        queue = deque([])
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        visited = 0
        while queue:
            node = queue.popleft()
            visited += 1

            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return visited == numCourses
