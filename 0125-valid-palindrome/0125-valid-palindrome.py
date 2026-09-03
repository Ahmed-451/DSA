class Solution:
    def isPalindrome(self, s: str) -> bool:
        filStr = "".join(filter(str.isalnum, s)).lower()
            
        #Check for palindrome
        l=0
        h=len(filStr)-1
        if len(filStr)==1:
            return True
        while l < h:
            if filStr[l]==filStr[h]:
                l+=1
                h-=1
            else:
                return False
        return True