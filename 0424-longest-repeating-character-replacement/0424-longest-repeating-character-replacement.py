class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        h=0
        l=0
        counts = [0]*26
        longest =0

        for h in range(n):
            counts[ord(s[h])-65]+=1

            while(h-l+1)- max(counts) > k:
                counts[ord(s[l])-65]-=1
                l+=1

            longest = max(longest,h-l+1)
        return longest

