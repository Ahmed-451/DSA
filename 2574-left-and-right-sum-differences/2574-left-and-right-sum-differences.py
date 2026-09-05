class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        left = 0
        answer = []
        for i in range(len(nums)):
            
            right = sum(nums)-nums[i]-left
            answer.append(abs(left-right))
            left += nums[i]
            
        return answer