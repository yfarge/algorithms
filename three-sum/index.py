class Solution:
    def threeSum(self, nums):
        nums.sort()
        triplets = []
        n = len(nums)
        for i in range(n):
            if i < n and i > 0 and nums[i - 1] == nums[i]:
                continue
            left, right = i + 1, n - 1
            first_num = nums[i]
            pair_target = 0 - first_num
            while left < right:
                pair_sum = nums[left] + nums[right]
                if pair_sum < pair_target:
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1
                elif pair_sum > pair_target:
                    right -= 1
                    while left < right and nums[right + 1] == nums[right]:
                        right -= 1
                else:
                    triplets.append([first_num, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while (left < right and nums[right + 1] == nums[right]
                           and nums[left - 1] == nums[left]):
                        left += 1
                        right -= 1
        return triplets
