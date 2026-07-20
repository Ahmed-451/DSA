class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        l = 0
        res = 1
        freq = {}

        for h in range(n):
            freq[fruits[h]] = freq.get(fruits[h],0)+1

            if len(freq)>2:
                while len(freq) >2:
                    freq[fruits[l]] -=1
                    if freq[fruits[l]] ==0:
                        del freq[fruits[l]]
                    l +=1
            
            elif len(freq) <= 2:
                res = max(res, h-l+1)
        return res 