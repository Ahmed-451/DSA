class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        dic = {}

        for i in range(n):
            dic[nums[i]] = dic.get(nums[i],0) +1
        
        if len(dic) == n:
            return False
        else:
            return True
        