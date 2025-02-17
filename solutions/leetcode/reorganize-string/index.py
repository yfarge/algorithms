from heapq import heapify, heappush, heappop
from collections import Counter, deque


class Solution:
    def reorganizeString(self, s: str) -> str:
        maxHeap = [(-count, char) for char, count in Counter(s).items()]
        heapify(maxHeap)
        queue = deque()
        res = []
        while maxHeap:
            count, char = heappop(maxHeap)
            res.append(char)
            if count < -1:
                queue.append((count + 1, char))

            if queue and res[-1] != queue[0][1]:
                heappush(maxHeap, queue.popleft())

        return "".join(res) if not queue else ""
