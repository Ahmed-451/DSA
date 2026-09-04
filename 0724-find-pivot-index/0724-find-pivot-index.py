class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        left =0
        right =0
        tsum = sum(nums)
        

        for i in range(len(nums)):
            if i ==0:
                pass
            else:
                left += nums[i-1]
            right = tsum-left-nums[i]
            if left == right:
                return i
        return -1