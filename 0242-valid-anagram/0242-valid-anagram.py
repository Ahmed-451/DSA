class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        a =s
        b = t
        if len(s)!=len(t):
            return False
        count1 = [0]*26
        count2 = [0]*26
        
        for i in s:
            count1[ord(i) - ord("a")] += 1
        

        for j in t:
            count2[ord(j) - ord("a")] += 1
        
        return count1 == count2
            