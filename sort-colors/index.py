from typing import *


def sortColors(nums: List[int]) -> None:
    counter = Counter(nums)

    i = 0
    for j in range(3):
        while counter[j]:
            nums[i] = j
            counter[j] -= 1
            i += 1


nums = [2, 1]

sortColors(nums)
print(nums)
