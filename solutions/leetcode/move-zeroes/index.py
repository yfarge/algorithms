from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0

        # write all non-zero numbers at the start of the array
        for read in range(len(nums)):
            if nums[read] != 0:
                nums[write] = nums[read]
                write += 1

        # set the rest of the array to zeroes
        for i in range(write, len(nums)):
            nums[i] = 0
