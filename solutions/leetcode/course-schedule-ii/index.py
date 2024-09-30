from typing import List
from collections import deque


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {course: [] for course in range(numCourses)}
        for a, b in prerequisites:
            graph[a].append(b)

        indegree = [0] * numCourses
        for course in range(numCourses):
            for dependency in graph[course]:
                indegree[dependency] += 1

        queue = deque([])
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        result = []
        visited = 0
        while queue:
            course = queue.popleft()
            result.append(course)
            visited += 1

            for dependency in graph[course]:
                indegree[dependency] -= 1
                if indegree[dependency] == 0:
                    queue.append(dependency)

        if visited != numCourses:
            return []
        return reversed(result)
