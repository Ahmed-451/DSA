class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        max_w = 0
        num_zero=0
        
        for h in range(n):
            if nums[h]==0:
                num_zero +=1
            
            while num_zero > k:
                if nums[l] == 0:
                    num_zero -=1
                l+=1
            max_w = max(max_w, h-l+1)
        
        return max_w