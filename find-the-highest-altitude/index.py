from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = max_altitude = 0
        for diff in gain:
            current_altitude += diff
            if current_altitude > max_altitude:
                max_altitude = current_altitude
        return max_altitude
