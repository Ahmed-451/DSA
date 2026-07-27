class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count1 = [0]*26
        count2 = [0]*26
        l = 0
        res = False
        for i in range(len(s1)):
            count1[ord(s1[i])-ord("a")] +=1


        
        for h in range(len(s2)):
            count2[ord(s2[h])-ord("a")]+=1

            if h-l+1 > len(s1):
                count2[ord(s2[l])-ord("a")]-=1
                l+=1

            if count1 == count2:
                res = True

        return res
            
            
            
            


