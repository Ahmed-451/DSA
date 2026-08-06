class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(nums)
        largest = nums[0]
        second = float('-inf')
        third = float('-inf')

        for i in range (n):
            if nums[i]==largest or nums[i]==second or nums[i]==third :
                continue

            if nums[i]>largest:
                third = second
                second = largest
                largest = nums[i]
            elif nums[i]>second:
                third = second
                second = nums[i]
            elif nums[i]>third:
                third = nums[i]
            
        if third == float('-inf'):
            return largest

        return third