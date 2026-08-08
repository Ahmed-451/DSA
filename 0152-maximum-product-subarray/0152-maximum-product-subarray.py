class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        bestmin=nums[0]
        bestmax=nums[0]
        res=nums[0]

        for i in range(1,len(nums)):

            v1 = nums[i]
            v2 = bestmin*nums[i]
            v3 = bestmax*nums[i]

            bestmax = max(v1,max(v2,v3))
            bestmin = min(v1,min(v2,v3))
            
            res = max(res, max(bestmax, bestmin))
        return res
