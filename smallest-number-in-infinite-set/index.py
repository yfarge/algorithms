from heap import heappop, heappush


class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.present = set()
        self.smallest = 1

    def popSmallest(self) -> int:
        if len(self.heap) > 0:
            smallest = heappop(self.heap)
            self.present.remove(smallest)
        else:
            smallest = self.smallest
            self.smallest += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.smallest and num not in self.present:
            heappush(self.heap, num)
            self.present.add(num)
