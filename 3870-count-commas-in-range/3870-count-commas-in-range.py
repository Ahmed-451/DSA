class Solution:
    def countCommas(self, n: int) -> int:
        ans=0
        if n >=1000:
            ans+=1
        elif n<1000:
            return 0
        ans += n - 1000
        return ans