class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        l = 0
        freq = {}
        res = 0
        for h in range(n):

            freq[s[h]] = freq.get(s[h], 0)+1

            while freq[s[h]] >=2:
                freq[s[l]]-=1
                if freq[s[l]]==0:
                    del(freq[s[l]])
                l +=1
            
            res = max(res, h-l+1)
        return res
        