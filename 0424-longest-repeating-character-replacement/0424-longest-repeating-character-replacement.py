class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        longest =0
        maxfreq =0
        counts = [0]*26
        l=0

        for h in range(n):
            counts[ord(s[h]) - ord("A")]+=1
            maxfreq = max(maxfreq, counts[ord(s[h]) - ord("A")] )

            while (h-l+1)-maxfreq >k:
                counts[ord(s[l])-ord("A")]-=1
                l +=1
            longest = max(longest,h-l+1)
        return longest