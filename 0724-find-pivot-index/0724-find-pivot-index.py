class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        left =0
        tsum = sum(nums)
        right = tsum - nums[0]        

        for i in range(len(nums)):
            right = tsum-left-nums[i]
            if left == right:
                return i
            left += nums[i]
            
            
        return -1