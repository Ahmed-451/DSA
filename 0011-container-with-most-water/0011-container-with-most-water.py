class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        h = n-1
        res =0
        area = 0
        while l <h:
            area = min(height[l],height[h]) * (h-l)
            res = max(res,area)

            if height[l]<=height[h]:
                l+=1
            else:
                h-=1
        return res
        
        