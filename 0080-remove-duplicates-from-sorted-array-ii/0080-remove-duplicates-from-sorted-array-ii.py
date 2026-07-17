class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)
        count = 1
        j = 1

        for i in range(1,n):

            if nums[i-1]==nums[i]:
                count +=1
            else:
                count = 1

            if count <= 2:
                nums[j] = nums[i]
                j+=1
        
        return j
        