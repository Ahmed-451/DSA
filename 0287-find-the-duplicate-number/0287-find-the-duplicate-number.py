class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        s = [False]*len(nums)

        for i in nums:
            if s[i]:
                return i
            else:
                s[i]=True