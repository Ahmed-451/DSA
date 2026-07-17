class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        of=0
        cm=1
        k=1

        for i in range(len(nums)-1):
            if nums[of]==nums[cm]:
                cm+=1
            else:
                #Swap
                temp = nums[cm]
                nums[cm]=nums[of+1]
                nums[of+1]=temp
                of+=1
                cm+=1
                k+=1

        return k