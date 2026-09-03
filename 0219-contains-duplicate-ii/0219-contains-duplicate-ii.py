class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        l=h=0

        while h < len(nums):
            if nums[h] in window:
                return True

            window.add(nums[h])
            h+=1

            if len(window)>k:
                window.remove(nums[l])
                l+=1
                
        return False
        
