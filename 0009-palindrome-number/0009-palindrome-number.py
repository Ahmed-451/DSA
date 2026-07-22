class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        rev =0
        l=0
        
        
        while n>0:
            l = n%10
            rev = rev*10+l
            n = n//10

        
        return rev == x