class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = []

        for i in nums:
            res.append(i)
        for j in range(n,0,-1):
            res.append(nums[j-1])

        return res