from typing import List
from collections import Counter, deque
from heapq import heapify, heappush, heappop


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = [-count for count in Counter(tasks).values()]
        heapify(maxHeap)

        time = 0
        queue = deque()
        while maxHeap or queue:
            time += 1
            if maxHeap:
                count = 1 + heappop(maxHeap)
                if count != 0:
                    queue.append((count, time + n))

            if queue and queue[0][1] == time:
                heappush(maxHeap, queue[0][0])
                queue.popleft()

        return time
