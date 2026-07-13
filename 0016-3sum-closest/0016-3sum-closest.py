class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        diff = float('inf')
        minsum = float('inf')

        for i in range(n-2):
            left = i+1
            right = n-1

            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s-target)<diff:
                    diff = abs(s - target)
                    minsum = s

                if s == target:
                    # left +=1
                    # right -=1
                    return s
                elif s < target:
                    left +=1
                elif s > target:
                    right -=1

        return int(minsum)