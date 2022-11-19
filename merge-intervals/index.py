class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        result = []
        intervals.sort()
        last_interval = [-1, -1]
        for i in range(len(intervals)):
            if self.isOverlap(intervals[i], last_interval):
                last_interval = [min(intervals[i][0], last_interval[0]),
                                 max(intervals[i][1], last_interval[1])]
            else:
                result.append(last_interval[:])
                last_interval = intervals[i]
        result.append(last_interval)
        return result[1:]

    def isOverlap(self, a: List[int], b: List[int]):
        return a[0] <= b[1] and a[1] >= b[0]
