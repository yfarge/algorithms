from typing import List
from collections import defaultdict


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
