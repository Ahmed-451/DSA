class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # First take normal kadens max sum subarray

        bestmax = nums[0]
        maxres = nums[0]

        for i in range(1,len(nums)):
            if nums[i]>bestmax + nums[i]:
                bestmax = nums[i]
            else:
                bestmax += nums[i]
            maxres = max(bestmax,maxres)

        # Now taking Min sum with Kadens Algo

        bestmin = nums[0]
        minres = nums[0]

        for i in range(1,len(nums)):
            if nums[i]>bestmin + nums[i]:
                bestmin += nums[i]
            else:
                bestmin = nums[i]
            minres = min(minres,bestmin)
        # Now we compare bestMax with total-bestMin and return the Maximun value with an edge case check
        if minres == sum(nums):
            return maxres
        else:
            return max(maxres,sum(nums)-minres)