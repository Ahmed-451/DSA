class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i = 0
        j = 0
        l = 0

        num3 = [0] * (m + n)

        while i < m and j < n:

            if nums1[i] <= nums2[j]:
                num3[l] = nums1[i]
                i += 1
            else:
                num3[l] = nums2[j]
                j += 1
            l += 1

        while i < m:
            num3[l] = nums1[i]
            i += 1
            l += 1

        while j < n:
            num3[l] = nums2[j]
            j += 1
            l += 1

        for k in range(m + n):
            nums1[k] = num3[k]