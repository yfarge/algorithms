from typing import List
from operator import itemgetter


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=itemgetter(0))
        answer = [intervals[0]]

        for i in range(1, len(intervals)):
            if answer[-1][1] < intervals[i][0]:
                answer.append(intervals[i])
            else:
                answer[-1][1] = max(answer[-1][1], intervals[i][1])

        return answer
