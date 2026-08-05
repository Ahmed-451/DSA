class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        res = 0

        for i in nums:
            tempEven = 0
            while i != 0:
                i = i//10
                tempEven +=1
            
            if tempEven %2 ==0:
                res +=1
        return res


        