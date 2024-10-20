from heapq import heappush, heappop


class MedianFinder:
    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        heappush(self.low, -num)

        if self.low and self.high and -self.low[0] > self.high[0]:
            value = heappop(self.low)
            heappush(self.high, -value)

        if len(self.low) > len(self.high) + 1:
            value = heappop(self.low)
            heappush(self.high, -value)
        elif len(self.high) > len(self.low):
            value = heappop(self.high)
            heappush(self.low, -value)

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        return (-self.low[0] + self.high[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
