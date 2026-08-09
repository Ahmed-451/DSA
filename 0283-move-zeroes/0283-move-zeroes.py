class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        l = 0
        for h in range(len(nums)):
            if nums[h] !=0:
                #Swap
                nums[l],nums[h] = nums[h],nums[l]
                l+=1        