class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        i = j = curr = last = 0
        n = (len(nums1) + len(nums2))
        b = n // 2
        while i + j <= b:
            last = curr
            v1 = nums1[i] if i < len(nums1) else float("inf")
            v2 = nums2[j] if j < len(nums2) else float("inf")
            if v1 <= v2:
                curr = v1
                i += 1
            else:
                curr = v2
                j += 1
        return curr if n % 2 else (curr + last) / 2.0
