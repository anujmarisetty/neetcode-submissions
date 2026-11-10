class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        l=0
        r=1
        while r<len(prices):
            curp=prices[r]-prices[l]
            maxp=max(maxp,curp)
            if prices[l]>=prices[r]:
                l=r
            r+=1
        return maxp