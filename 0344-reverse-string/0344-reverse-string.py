class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l = 0
        n = len(s)
        h = n-1

        while l < h:
            #swap
            temp = s[l]
            s[l]=s[h]
            s[h] = temp

            l +=1
            h -=1
        
