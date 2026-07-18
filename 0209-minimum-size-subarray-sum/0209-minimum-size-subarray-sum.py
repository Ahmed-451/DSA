class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n = len(nums)
        h = 0
        l = 0
        length = 0
        sum = 0
        res = float('inf')

        while h<n:
            sum = sum + nums[h]

            while sum >= target:
                length = h - l +1
                res = min(res,length)
                sum = sum - nums[l]

                l +=1
            h +=1

        if res == float('inf'):
            res = 0

        return res
        