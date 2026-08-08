class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        best = nums[0]
        res = nums[0]

        for i in range(1,len(nums)):
            if nums[i] < best+nums[i]:
                best += nums[i]
            else:
                best = nums[i]
        
            if best> res:
                res = best
        return res