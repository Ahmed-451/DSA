class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        left = 0
        right = sum(nums)-nums[0]
        answer = []
        for i in range(len(nums)):
            
            if i ==0:
                pass
            else:
                left += nums[i-1]
                right = sum(nums)-nums[i]-left

            answer.append(abs(left-right))
        return answer