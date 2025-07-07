class Solution:
    def maxProfit(self, prices: List[int]) -> int:


     l=len(prices)
     max_p=0
     buy=prices[0]
     for i in range(1,l):
        ma=max(max_p,prices[i]-buy)
        if buy > prices[i]:
            buy =prices[i]
        else:
            max_p=max(max_p,prices[i]-buy)
     return max_p