class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        s = 0
        freq = {}
        freq[0] = 1
        for i in range(len(nums)):
            s += nums[i]
            ques = (s-k)
            
            f = freq.get(ques,0)
            freq[s]=freq.get(s,0)+1
            ans += f
        return ans
