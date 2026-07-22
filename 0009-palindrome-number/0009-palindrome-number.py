class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        rev =0
        l=0
        
        if x < 0:
            return False
        while n>0:
            l = n%10
            rev = rev*10+l
            n = n//10

        
        return rev == x