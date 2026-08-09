class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        bestmax = nums[0]
        bestmin = nums[0]
        maxres = nums[0]
        minres = nums[0]

        #Max SubArray
        for i in range(1,len(nums)):
            if nums[i]>bestmax+nums[i]:
                bestmax = nums[i]
            else:
                bestmax += nums[i]
            maxres = max(maxres,bestmax)
        
        #Min SubArray
        for i in range(1,len(nums)):
            if nums[i]>bestmin+nums[i]:
                bestmin += nums[i]
            else:
                bestmin = nums[i]
            minres = min(minres,bestmin)

        minres = abs(minres)
        return max(maxres,minres)
