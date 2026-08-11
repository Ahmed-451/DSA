class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        l = 0
        h = k-1
        res = float('-inf')
        cursum =0
        for i in range(k):
            cursum += nums[i]

        res = cursum

        # Slide the window
        while h + 1 < len(nums):
            cursum -= nums[l]
            l += 1

            h += 1
            cursum += nums[h]

            res = max(res, cursum)

        return res / k