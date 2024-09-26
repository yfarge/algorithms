from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map[key]
        if len(values) == 0:
            return ""

        low, high = 0, len(values) - 1
        while low <= high:
            mid = (low + high) // 2

            if values[mid][0] < timestamp:
                low = mid + 1
            elif values[mid][0] > timestamp:
                high = mid - 1
            else:
                return values[mid][1]

        if high >= 0:
            return values[high][1]

        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
