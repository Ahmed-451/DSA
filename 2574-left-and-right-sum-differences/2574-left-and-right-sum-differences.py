class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:

        left = 0
        total = sum(nums)
        answer = []
        for i in range(len(nums)):
            right = total-nums[i]-left
            answer.append(abs(left-right))
            left += nums[i]
            
        return answer