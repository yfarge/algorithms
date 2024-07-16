from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = [False] * len(rooms)
        stack = [0]

        while stack:
            current_room = stack.pop()
            seen[current_room] = True

            for room in rooms[current_room]:
                if not seen[room]:
                    stack.append(room)

        return seen
