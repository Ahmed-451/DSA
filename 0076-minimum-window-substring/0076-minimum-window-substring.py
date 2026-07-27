class Solution:
    def minWindow(self, s: str, t: str) -> str:
    
        n = len(s)
        res = float('inf')
        have = [0]*256
        need = [0]*256
        l=0
        formed = 0
        required = 0
        start = 0
        
        if len(s)<len(t):
            return ""

        for i in range(len(t)):
            if need[ord(t[i])] ==0:
                required +=1
            need[ord(t[i])]+=1
        

        for h in range(n):
            have[ord(s[h])]+=1

            if have[ord(s[h])] == need[ord(s[h])]:
                formed +=1
            
            while formed == required:
                if res > h-l+1:
                    res = h-l+1
                    start = l

                char = s[l]
                have[ord(s[l])]-=1
                if have[ord(char)] < need[ord(char)]:
                    formed -=1
                l+=1
        if res == float('inf'):
            return ""
        else:
            return s[start:start+res]

