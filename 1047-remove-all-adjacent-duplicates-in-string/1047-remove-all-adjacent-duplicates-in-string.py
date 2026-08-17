class Solution:
    def removeDuplicates(self, s: str) -> str:

        res = [s[0]]
        
        for i in range(1,len(s)):
            
            if len(res)==0:
                res.append(s[i])
            else:
                if s[i] != res[-1]:
                    res.append(s[i])
                else:
                    res.pop()
                
        return "".join(res)