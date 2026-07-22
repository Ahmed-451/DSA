class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit =0
        buy = float('inf')

        for i in prices:
            if i < buy:
                buy = i
            elif (i - buy) > profit:
                profit = i - buy
        return profit